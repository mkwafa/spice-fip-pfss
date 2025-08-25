
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
	mask_array_62702784 = (x > 700.659688026) & (x < 711.581592026);sub_x_62702784 = x[mask_array_62702784];sum[mask_array_62702784] += arg_14
	mask_array_50481589 = (x > 745.615025026) & (x < 753.4163850260002);sub_x_50481589 = x[mask_array_50481589];sum[mask_array_50481589] += arg_15
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9,arg_10,arg_11,arg_12,arg_13,arg_14,arg_15):
	l=16
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_46095844 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_70697877 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_73219604 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	exp_58504396 = np.exp(-(x-(arg_12+-1.82000000000005))**2/(2*(arg_13+0)**2))
	exp_35177431 = np.exp(-(x-(arg_7+43.51999999999998))**2/(2*(arg_8+0)**2))
	exp_86159342 = np.exp(-(x-arg_12)**2/(2*arg_13**2))
	mask_array_74210742 = (x > 700.659688026) & (x < 711.581592026);sub_x_74210742 = x[mask_array_74210742]
	mask_array_26628125 = (x > 745.615025026) & (x < 753.4163850260002);sub_x_26628125 = x[mask_array_26628125]
	
	jac[:,0]= exp_46095844
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_46095844
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_46095844
	jac[:,3]= exp_70697877
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_70697877
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_70697877
	jac[:,6]= exp_73219604
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_73219604 + arg_10*(x-(arg_7+43.51999999999998))   /((arg_8+0)**2) * exp_35177431
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_73219604 + arg_10*(x-(arg_7+43.51999999999998))**2/((arg_8+0)**3) * exp_35177431
	jac[:,9]= exp_58504396
	jac[:,10]= exp_35177431
	jac[:,11]= exp_86159342
	jac[:,12]= arg_9*(x-(arg_12+-1.82000000000005))   /((arg_13+0)**2) * exp_58504396 + arg_11*(x-arg_12)   /(arg_13**2) * exp_86159342
	jac[:,13]= arg_9*(x-(arg_12+-1.82000000000005))**2/((arg_13+0)**3) * exp_58504396 + arg_11*(x-arg_12)**2/(arg_13**3) * exp_86159342
	jac[mask_array_74210742,14]= 1
	jac[mask_array_26628125,15]= 1
	
	
	return jac