
# Function definition
import numpy as np
from numba import jit

def model_function(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9,arg_10,arg_11,arg_12,arg_13,arg_14,arg_15):
	l=16
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	sum = np.zeros((len(x), ),dtype=np.float64)
	sum+=arg_0*np.exp(-(x-arg_1)**2/(2*arg_2**2))
	sum+=arg_3*np.exp(-(x-arg_4)**2/(2*arg_5**2))
	sum+=arg_6*np.exp(-(x-arg_7)**2/(2*arg_8**2))
	sum+=arg_9*np.exp(-(x-(arg_12+-1.82000000000005))**2/(2*(arg_13+0)**2))
	sum+=arg_10*np.exp(-(x-(arg_7+43.51999999999998))**2/(2*(arg_8+0)**2))
	sum+=arg_11*np.exp(-(x-arg_12)**2/(2*arg_13**2))
	mask_array_12650949 = (x > 700.659688026) & (x < 711.581592026);sub_x_12650949 = x[mask_array_12650949];sum[mask_array_12650949] += arg_14
	mask_array_3215905 = (x > 745.615025026) & (x < 753.4163850260002);sub_x_3215905 = x[mask_array_3215905];sum[mask_array_3215905] += arg_15
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9,arg_10,arg_11,arg_12,arg_13,arg_14,arg_15):
	l=16
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_47298309 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_3841560 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_5957662 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	exp_18382198 = np.exp(-(x-(arg_12+-1.82000000000005))**2/(2*(arg_13+0)**2))
	exp_53758207 = np.exp(-(x-(arg_7+43.51999999999998))**2/(2*(arg_8+0)**2))
	exp_35311510 = np.exp(-(x-arg_12)**2/(2*arg_13**2))
	mask_array_75626341 = (x > 700.659688026) & (x < 711.581592026);sub_x_75626341 = x[mask_array_75626341]
	mask_array_44023609 = (x > 745.615025026) & (x < 753.4163850260002);sub_x_44023609 = x[mask_array_44023609]
	
	jac[:,0]= exp_47298309
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_47298309
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_47298309
	jac[:,3]= exp_3841560
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_3841560
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_3841560
	jac[:,6]= exp_5957662
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_5957662 + arg_10*(x-(arg_7+43.51999999999998))   /((arg_8+0)**2) * exp_53758207
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_5957662 + arg_10*(x-(arg_7+43.51999999999998))**2/((arg_8+0)**3) * exp_53758207
	jac[:,9]= exp_18382198
	jac[:,10]= exp_53758207
	jac[:,11]= exp_35311510
	jac[:,12]= arg_9*(x-(arg_12+-1.82000000000005))   /((arg_13+0)**2) * exp_18382198 + arg_11*(x-arg_12)   /(arg_13**2) * exp_35311510
	jac[:,13]= arg_9*(x-(arg_12+-1.82000000000005))**2/((arg_13+0)**3) * exp_18382198 + arg_11*(x-arg_12)**2/(arg_13**3) * exp_35311510
	jac[mask_array_75626341,14]= 1
	jac[mask_array_44023609,15]= 1
	
	
	return jac