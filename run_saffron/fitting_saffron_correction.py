import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path 
from astropy.io import fits
def find_file(name, base_path= Path(r"/archive/SOLAR-ORBITER/SPICE/fits/") ):
  date = name.split('_')[3]
  year = date[:4]
  month = date[4:6]
  day = date[6:8]
  level = "level"+name.split('_')[1][1]
  path = base_path/level/year/month/day/name
  return path

import sospice 
import numpy as np 
# plot all the dates of the selected files
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime
from matplotlib.dates import DateFormatter
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np
from pathlib import Path
from scipy.interpolate import interp1d
from saffron.manager import Manager
from saffron.utils import get_input_template
import numpy as np
import warnings
import os
import matplotlib.pyplot as plt
import astropy.units as u
from saffron.utils.utils import colored_text
import os

np.seterr(invalid='ignore') 
warnings.filterwarnings("ignore", category=RuntimeWarning)



def get_path(cat ,base_folder = Path('/archive/SOLAR-ORBITER/SPICE/fits/')):
    base_folder =Path(base_folder)
    
    list_paths = [ 
        (base_folder / cat['FILE_PATH'].iloc[i]) / cat.FILENAME.iloc[i] 
        for i in range(len(cat))
      
    ]
    
    return list_paths

def search_lines_by_ion_state(model,ion_name):
  ions = []
  for ind in range(len(model.functions_names['gaussian'])):
    if ion_name.lower() == model.functions_names['gaussian'][ind][0]:
      ions.append(
        {
          "index":ind,
          "name":model.functions_names['gaussian'][ind][0],
          'wvl':model.functions_names['gaussian'][ind][1],
        })
      
  return ions

def search_lines_by_element_name(model,element_name):
  ions = []
  for ind in range(len(model.functions_names['gaussian'])):
    if element_name.lower() == model.functions_names['gaussian'][ind][0].split('_')[0]:
      ions.append(
        {
          "index":ind,
          "name":model.functions_names['gaussian'][ind][0],
          'wvl':model.functions_names['gaussian'][ind][1],
        })
      
  return ions

def create_lock_lines(model,element=None,ion_state=None,closest_wvl = None):
  """
  takes the model and the element name and its ion state number optional and searth and the closest wavelength obligatory than search for all the elements or element at the given ion state and then search for functions names of the chosen lines (contai the name and the wavelngths) and all classifie them and from that generate Delta wavelength between the closest and each of the rest then prepare the locking dictionary of the form 
  locking_list = [
      {
        "param_1" : {"model_type":'gaussian',"element_index":7,"parameter":"x"},
        "param_2" : {"model_type":'gaussian',"element_index":6,"parameter":"x"},
        "lock_protocol" : {"operation":"add",'value':diff_wvl_O4_O42},
        },
      {
      "param_1" : {"model_type":'gaussian',"element_index":7,"parameter":"s"},
      "param_2" : {"model_type":'gaussian',"element_index":6,"parameter":"s"},
      "lock_protocol" : {"operation":"add",'value':0},
      },
      ]
  param1 is the parameter of the line that will be locked to param2 of the line and value in x is delta wvl betwwn parms1 and 2 so that params1 = params2 + value
  """
  
  #1. assert closest_wvl is not None
  assert closest_wvl is not None, "Closest_wvl is required"
  assert element is not None or ion_state is not None, "Either element or ion_state is required"
  #2. search for the lines of the element and ion_state
  if ion_state is not None:
    lines = search_lines_by_ion_state(model,ion_state)
  else:
    lines = search_lines_by_element_name(model,element) 
  #3. get all the function names of the model
  functions_names = model.functions_names['gaussian'] 
  #4 search for the closest wavelength reference line 
  all_wavelength = np.array([line['wvl'] for line in lines])
  ref_line = lines[np.argmin(np.abs(all_wavelength - closest_wvl))]
  
  #5. generating lock dictionary 
  locking_list = []
  for line in lines:
    if line['index']!= ref_line['index']:
      diff_wvl = line['wvl'] - ref_line['wvl']
      locking_list.append(
        {
          "param_1" : {"model_type":'gaussian',"element_index":line['index'],"parameter":"x"},
          "param_2" : {"model_type":'gaussian',"element_index":ref_line['index'],"parameter":"x"},
          "lock_protocol" : {"operation":"add",'value':diff_wvl},
          }
        )
      locking_list.append(
        {
          "param_1" : {"model_type":'gaussian',"element_index":line['index'],"parameter":"s"},
          "param_2" : {"model_type":'gaussian',"element_index":ref_line['index'],"parameter":"s"},
          "lock_protocol" : {"operation":"add",'value':0},
          },
        )
  return locking_list

def my_TS_series_locker(window,session,verbose=1):
  work_model = window.model
  mg_lock =  create_lock_lines(model = work_model ,element='mg',closest_wvl=706.2)
  s_lock = create_lock_lines(model = work_model , element='s', closest_wvl=786)
  o_lock = create_lock_lines(model = work_model , element='o', closest_wvl=788)
  locking_list = mg_lock + s_lock + o_lock

  for lock in locking_list:
    session.lock("fuse",0,**lock)
  work_model = window.model

  if True:
    from scipy.optimize import curve_fit
    try: _data = np.nanmean(np.concatenate([hdu.data.copy() for hdu in window.hdu],axis=1),axis=(0,2,3))
    except: _data = np.nanmean(hdu.data.copy(),axis=(0,2,3))
    specaxis = window.specaxis
    x_plot = np.arange(len(_data))
    # x_plot = specaxis

    if verbose>=1: plt.figure(figsize=(10,5))
    if verbose>=1: plt.step(x_plot,_data,lw=1.5,c='black',label='raw')
    params= work_model.get_lock_params()
    if verbose>=1: plt.step(x_plot,work_model.callables['function' ](specaxis,*params),label='locked model')


    x = specaxis[(~np.isnan(_data))&(~np.isnan(_data))]
    y = _data[(~np.isnan(_data))&(~np.isnan(_data))]
    curv_fit_params, curv_fit_cov = curve_fit(
      work_model.callables['function' ],
      x,
      y,
      p0=params,
      jac = work_model.callables['jacobian' ],
      bounds = work_model.bounds,
      )
    
    if verbose>=1: plt.step(x_plot,work_model.callables['function' ](specaxis,*curv_fit_params),label='curve_fit model')
    if verbose>=1: plt.yscale('log')
    if verbose>=1: plt.ylim(bottom=0.01)
    
    window.model.set_lock_params(curv_fit_params)
    
    for ind,x in enumerate(work_model.get_unlock_params()[work_model.get_unlock_quentities()=="x"]):
      if True:
        name = work_model.functions_names['gaussian'][ind]
        # i think it is better to go back to the interpolation method
        f = interp1d(specaxis, x_plot, kind='cubic')
        try:x_ = f(x)
        except: 
          # in case this is out of the interpolation range
          #search the closest value in specaxis 
          x_1_idx = np.argmin(np.abs(specaxis-x))
          # search the second closest value to x 
          x_2_idx = np.argsort(np.abs(specaxis-x))[1]
          # create a small_sett for polyfit of 1 degree
          sub_x = specaxis[[x_1_idx,x_2_idx]]
          sub_x_plot = x_plot[[x_1_idx,x_2_idx]]
          f = np.poly1d(np.polyfit(sub_x,sub_x_plot,1))
          x_ = f(x)
        
      if verbose>=1: 
        if x in curv_fit_params:
          plt.axvline(x_,linestyle='--',color='k',label=f'{name[0]}:{name[1]}')
        else:
          plt.axvline(x_,linestyle=':',color='cyan',label=f'{name[0]}:{name[1]}')
    
    #place the legend in the top of the figure()
    if verbose>=1: plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=6)
    if verbose>=4:
      # create file name based on data now fit_inits_YYMMDDTHHMMSS.png
      file_name = f'fit_inits_{datetime.now().strftime("%Y%m%dT%H%M%S")}.png' 
      plt.savefig(Path("./tmp")/file_name)
  return locking_list, curv_fit_params


def my_COMPO_series_locker(window,verbose=4):
  work_model = window.model
  mg_lock =  create_lock_lines(model = work_model ,element='mg',closest_wvl=706.02)
  s_lock = create_lock_lines(model = work_model , ion_state='s_4', closest_wvl=750.22)
  # o_lock = create_lock_lines(model = work_model , element='o', closest_wvl=703.87)
  locking_list = mg_lock + s_lock 
  
  for lock in locking_list:
    lock['param_1']['model_type'] = 'gaussian'
    lock['param_2']['model_type'] = 'gaussian'
    work_model.lock(**lock)

  if True:
    from scipy.optimize import curve_fit
    try: _data = np.nanmean(np.concatenate([hdu.data.copy() for hdu in window.hdu],axis=1),axis=(0,2,3))
    except: _data = np.nanmean(hdu.data.copy(),axis=(0,2,3))
    specaxis = window.specaxis
    x_plot = np.arange(len(_data))
    # x_plot = specaxis

    if verbose>=1: plt.figure(figsize=(10,5))
    if verbose>=1: plt.step(x_plot,_data,lw=1.5,c='black',label='raw')
    params= work_model.get_lock_params()
    if verbose>=1: plt.step(x_plot,work_model.callables['function' ](specaxis,*params),label='locked model')
    
    bounds_rules = work_model.bounds_rules 
    
    work_model.set_bounds(
                kwargs = {
                    "I": [0, 1000], 
                    "x": [["ref-add", -0.1], ["ref-add", 0.1]], 
                    "s": [0.20, 0.6], 
                    "B": [-10, 10]
                    }
            )

    x = specaxis[(~np.isnan(_data))&(~np.isnan(_data))]
    y = _data[(~np.isnan(_data))&(~np.isnan(_data))]
    curv_fit_params, curv_fit_cov = curve_fit(
      work_model.callables['function' ],
      x,
      y,
      p0=params,
      jac = work_model.callables['jacobian' ],
      bounds = work_model.bounds,
      # sigma = np.sqrt(np.abs(y)),
      )
    
    if verbose>=1: plt.step(x_plot,work_model.callables['function' ](specaxis,*curv_fit_params),label='curve_fit model')
    if verbose>=1: plt.yscale('log')
    if verbose>=1: plt.ylim(bottom=0.01)
    
    work_model.set_lock_params(curv_fit_params)
    
    for ind,x in enumerate(work_model.get_unlock_params()[work_model.get_unlock_quentities()=="x"]):
      if True:
        name = work_model.functions_names['gaussian'][ind]
        # i think it is better to go back to the interpolation method
        f = interp1d(specaxis, x_plot, kind='cubic')
        try:x_ = f(x)
        except: 
          # in case this is out of the interpolation range
          #search the closest value in specaxis 
          x_1_idx = np.argmin(np.abs(specaxis-x))
          # search the second closest value to x 
          x_2_idx = np.argsort(np.abs(specaxis-x))[1]
          # create a small_sett for polyfit of 1 degree
          sub_x = specaxis[[x_1_idx,x_2_idx]]
          sub_x_plot = x_plot[[x_1_idx,x_2_idx]]
          f = np.poly1d(np.polyfit(sub_x,sub_x_plot,1))
          x_ = f(x)
        
      if verbose>=1: 
        if x in curv_fit_params:
          plt.axvline(x_,linestyle='--',color='k',label=f'{name[0]}:{name[1]}')
        else:
          plt.axvline(x_,linestyle=':',color='cyan',label=f'{name[0]}:{name[1]}')
    
    #place the legend in the top of the figure()
    if verbose>=1: plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=6)
    if verbose>=4:
      # create file name based on data now fit_inits_YYMMDDTHHMMSS.png
      file_name = f'fit_inits_{datetime.now().strftime("%Y%m%dT%H%M%S")}.png' 
      plt.savefig(Path("./tmp")/file_name)
    
    window.model = work_model
    window.model.set_bounds(bounds_rules)
    
  return locking_list, curv_fit_params




def Wafa_COMPO_series_locker(window,verbose=4):
  work_model = window.model
  if len(search_lines_by_ion_state(model = work_model, ion_name = 'mg_9')) >=2:
    mg_lock =  create_lock_lines(model = work_model ,element='mg',closest_wvl=706.02)
  else: 
    print("There is less than 2 Mg_9 lines. Can't lock" )
    mg_lock = []
  
  if len(search_lines_by_ion_state(model = work_model, ion_name = 's_4')) >=2:
    s_lock = create_lock_lines(model = work_model , ion_state='s_4', closest_wvl=750.22)
  else: 
    print("There is less than 2 s_4 lines. Can't lock" )
    s_lock = []
  # o_lock = create_lock_lines(model = work_model , element='o', closest_wvl=703.87)
  locking_list = mg_lock + s_lock 
  
  for lock in locking_list:
    lock['param_1']['model_type'] = 'gaussian'
    lock['param_2']['model_type'] = 'gaussian'
    work_model.lock(**lock)

  if True:
    from scipy.optimize import curve_fit
    try: _data = np.nanmean(np.concatenate([hdu.data.copy() for hdu in window.hdu],axis=1),axis=(0,2,3))
    except: _data = np.nanmean(hdu.data.copy(),axis=(0,2,3))
    specaxis = window.specaxis
    x_plot = np.arange(len(_data))
    # x_plot = specaxis

    if verbose>=1: plt.figure(figsize=(10,5))
    if verbose>=1: plt.step(x_plot,_data,lw=1.5,c='black',label='raw')
    params= work_model.get_lock_params()
    if verbose>=1: plt.step(x_plot,work_model.callables['function' ](specaxis,*params),label='locked model')
    
    bounds_rules = work_model.bounds_rules 
    
    work_model.set_bounds(
                kwargs = {
                    "I": [0, 1000], 
                    "x": [["ref-add", -0.1], ["ref-add", 0.1]], 
                    "s": [0.20, 0.6], 
                    "B": [-10, 10]
                    }
            )

    x = specaxis[(~np.isnan(_data))&(~np.isnan(_data))]
    y = _data[(~np.isnan(_data))&(~np.isnan(_data))]
    curv_fit_params, curv_fit_cov = curve_fit(
      work_model.callables['function' ],
      x,
      y,
      p0=params,
      jac = work_model.callables['jacobian' ],
      bounds = work_model.bounds,
      # sigma = np.sqrt(np.abs(y)),
      )
    
    if verbose>=1: plt.step(x_plot,work_model.callables['function' ](specaxis,*curv_fit_params),label='curve_fit model')
    if verbose>=1: plt.yscale('log')
    if verbose>=1: plt.ylim(bottom=0.01)
    
    work_model.set_lock_params(curv_fit_params)
    
    for ind,x in enumerate(work_model.get_unlock_params()[work_model.get_unlock_quentities()=="x"]):
      if True:
        name = work_model.functions_names['gaussian'][ind]
        # i think it is better to go back to the interpolation method
        f = interp1d(specaxis, x_plot, kind='cubic')
        try:x_ = f(x)
        except: 
          # in case this is out of the interpolation range
          #search the closest value in specaxis 
          x_1_idx = np.argmin(np.abs(specaxis-x))
          # search the second closest value to x 
          x_2_idx = np.argsort(np.abs(specaxis-x))[1]
          # create a small_sett for polyfit of 1 degree
          sub_x = specaxis[[x_1_idx,x_2_idx]]
          sub_x_plot = x_plot[[x_1_idx,x_2_idx]]
          f = np.poly1d(np.polyfit(sub_x,sub_x_plot,1))
          x_ = f(x)
        
      if verbose>=1: 
        if x in curv_fit_params:
          plt.axvline(x_,linestyle='--',color='k',label=f'{name[0]}:{name[1]}')
        else:
          plt.axvline(x_,linestyle=':',color='cyan',label=f'{name[0]}:{name[1]}')
    
    #place the legend in the top of the figure()
    if verbose>=1: plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=6)
    if verbose>=4:
      # create file name based on data now fit_inits_YYMMDDTHHMMSS.png
      file_name = f'fit_inits_{datetime.now().strftime("%Y%m%dT%H%M%S")}.png' 
      plt.savefig(Path("./tmp")/file_name)
    
    window.model = work_model
    window.model.set_bounds(bounds_rules)
    
  return locking_list, curv_fit_params