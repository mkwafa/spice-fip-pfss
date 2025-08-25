import os
from pathlib import Path
from saffron.manager import Manager
from fitting_saffron_correction import *
# from saffron.utils import get_input_template
# get_input_template(where='./input.json')

# Paths to SPICE FITS files
# path_list_TS = [
#     r"/archive/SOLAR-ORBITER/SPICE/fits/level2/2025/04/06/solo_L2_spice-n-sit_20250406T005822_V01_318767310-000.fits"
# ]

path_list_Compo = [
    r"/archive/SOLAR-ORBITER/SPICE/fits/level2/2025/03/21/solo_L2_spice-n-ras_20250321T040142_V04_318767203-000.fits",
    r"/archive/SOLAR-ORBITER/SPICE/fits/level2/2025/04/01/solo_L2_spice-n-ras_20250401T200531_V06_318767286-000.fits",
    r"/archive/SOLAR-ORBITER/SPICE/fits/level2/2025/04/03/solo_L2_spice-n-ras_20250403T180532_V03_318767296-000.fits",
    r"/archive/SOLAR-ORBITER/SPICE/fits/level2/2022/10/29/solo_L2_spice-n-ras_20221029T064536_V22_150995442-000.fits",
    r"/archive/SOLAR-ORBITER/SPICE/fits/level2/2024/03/30/solo_L2_spice-n-ras_20240330T075931_V22_251658408-000.fits",
    r"/archive/SOLAR-ORBITER/SPICE/fits/level2/2024/03/30/solo_L2_spice-n-ras_20240330T075931_V22_251658408-000.fits",  # duplicate
    r"/archive/SOLAR-ORBITER/SPICE/fits/level2/2023/10/12/solo_L2_spice-n-ras_20231012T034900_V22_218104076-000.fits",
]

# print(f"Found {len(path_list_Compo+path_list_TS)} raster files.")

# conv = spatial convolution (smoothing in x/y)
for conv in [6]:
    session = Manager("./input.json")
    session.selected_fits = path_list_Compo
    session.convolution_extent_list = np.array([conv])
    session.build_rasters()
    print("Build rasters finished")

    session.run_preparations()
    session.fuse_windows([0,1])

    try: 
        locking_list
    except:
        # lock spectral lines for fitting
        locking_list, curv_fit_params = Wafa_COMPO_series_locker(session.rasters[0].fused_windows[0], verbose=4)
        session.rasters[0].fused_windows = []
        session.rasters[0].fuse_windows(0,1)
            
    for lock in locking_list:
        session.lock("fuse",0,**lock)

    print("Run preparations finished")
    session.fit_manager()
    print("Fit manager finished")
del locking_list


# Example for sit-and-stare:
# conv = spatial convolution, tconv = temporal convolution (averaging over exposures)
# for conv, tconv in [[6,4]]:
#     session = Manager("./input.json")
#     session.selected_fits = path_list_TS
#     session.convolution_extent_list = np.array([conv])
#     session.t_convolution_index = tconv
#     session.build_rasters()
#     session.run_preparations()
#     session.rasters[0].fused_windows = []
#     session.fuse_windows([0,1,4])
#     locking_list, curv_fit_params = my_TS_series_locker(session.rasters[0].fused_windows[0], session, verbose=4)
#     for lock in locking_list:
#         session.lock("fuse",0,**lock)
#     session.fit_manager()
