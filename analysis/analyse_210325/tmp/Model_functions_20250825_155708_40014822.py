
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
	mask_array_44040529 = (x > 700.659688026) & (x < 711.581592026);sub_x_44040529 = x[mask_array_44040529];sum[mask_array_44040529] += arg_14
	mask_array_20872525 = (x > 745.615025026) & (x < 753.4163850260002);sub_x_20872525 = x[mask_array_20872525];sum[mask_array_20872525] += arg_15
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9,arg_10,arg_11,arg_12,arg_13,arg_14,arg_15):
	l=16
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_62855198 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_95312916 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_40663666 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	exp_55312517 = np.exp(-(x-(arg_12+-1.82000000000005))**2/(2*(arg_13+0)**2))
	exp_8267269 = np.exp(-(x-(arg_7+43.51999999999998))**2/(2*(arg_8+0)**2))
	exp_54775609 = np.exp(-(x-arg_12)**2/(2*arg_13**2))
	mask_array_54711846 = (x > 700.659688026) & (x < 711.581592026);sub_x_54711846 = x[mask_array_54711846]
	mask_array_77804964 = (x > 745.615025026) & (x < 753.4163850260002);sub_x_77804964 = x[mask_array_77804964]
	
	jac[:,0]= exp_62855198
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_62855198
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_62855198
	jac[:,3]= exp_95312916
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_95312916
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_95312916
	jac[:,6]= exp_40663666
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_40663666 + arg_10*(x-(arg_7+43.51999999999998))   /((arg_8+0)**2) * exp_8267269
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_40663666 + arg_10*(x-(arg_7+43.51999999999998))**2/((arg_8+0)**3) * exp_8267269
	jac[:,9]= exp_55312517
	jac[:,10]= exp_8267269
	jac[:,11]= exp_54775609
	jac[:,12]= arg_9*(x-(arg_12+-1.82000000000005))   /((arg_13+0)**2) * exp_55312517 + arg_11*(x-arg_12)   /(arg_13**2) * exp_54775609
	jac[:,13]= arg_9*(x-(arg_12+-1.82000000000005))**2/((arg_13+0)**3) * exp_55312517 + arg_11*(x-arg_12)**2/(arg_13**3) * exp_54775609
	jac[mask_array_54711846,14]= 1
	jac[mask_array_77804964,15]= 1
	
	
	return jac