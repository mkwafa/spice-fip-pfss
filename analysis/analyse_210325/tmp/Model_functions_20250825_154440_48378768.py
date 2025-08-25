
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
	mask_array_62309291 = (x > 700.659688026) & (x < 711.581592026);sub_x_62309291 = x[mask_array_62309291];sum[mask_array_62309291] += arg_14
	mask_array_15888571 = (x > 745.615025026) & (x < 753.4163850260002);sub_x_15888571 = x[mask_array_15888571];sum[mask_array_15888571] += arg_15
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9,arg_10,arg_11,arg_12,arg_13,arg_14,arg_15):
	l=16
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_78402798 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_96442163 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_76283437 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	exp_87619300 = np.exp(-(x-(arg_12+-1.82000000000005))**2/(2*(arg_13+0)**2))
	exp_81557575 = np.exp(-(x-(arg_7+43.51999999999998))**2/(2*(arg_8+0)**2))
	exp_64136478 = np.exp(-(x-arg_12)**2/(2*arg_13**2))
	mask_array_94856894 = (x > 700.659688026) & (x < 711.581592026);sub_x_94856894 = x[mask_array_94856894]
	mask_array_86802709 = (x > 745.615025026) & (x < 753.4163850260002);sub_x_86802709 = x[mask_array_86802709]
	
	jac[:,0]= exp_78402798
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_78402798
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_78402798
	jac[:,3]= exp_96442163
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_96442163
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_96442163
	jac[:,6]= exp_76283437
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_76283437 + arg_10*(x-(arg_7+43.51999999999998))   /((arg_8+0)**2) * exp_81557575
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_76283437 + arg_10*(x-(arg_7+43.51999999999998))**2/((arg_8+0)**3) * exp_81557575
	jac[:,9]= exp_87619300
	jac[:,10]= exp_81557575
	jac[:,11]= exp_64136478
	jac[:,12]= arg_9*(x-(arg_12+-1.82000000000005))   /((arg_13+0)**2) * exp_87619300 + arg_11*(x-arg_12)   /(arg_13**2) * exp_64136478
	jac[:,13]= arg_9*(x-(arg_12+-1.82000000000005))**2/((arg_13+0)**3) * exp_87619300 + arg_11*(x-arg_12)**2/(arg_13**3) * exp_64136478
	jac[mask_array_94856894,14]= 1
	jac[mask_array_86802709,15]= 1
	
	
	return jac