
# Function definition
import numpy as np
from numba import jit

def model_function(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9):
	l=10
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	sum = np.zeros((len(x), ),dtype=np.float64)
	sum+=arg_0*np.exp(-(x-arg_1)**2/(2*arg_2**2))
	sum+=arg_3*np.exp(-(x-arg_4)**2/(2*arg_5**2))
	sum+=arg_6*np.exp(-(x-arg_7)**2/(2*arg_8**2))
	mask_array_23208873 = (x > 984.5796120610001) & (x < 995.9347520609999);sub_x_23208873 = x[mask_array_23208873];sum[mask_array_23208873] += arg_9
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9):
	l=10
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_40623151 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_64133599 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_57725979 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	mask_array_50744021 = (x > 984.5796120610001) & (x < 995.9347520609999);sub_x_50744021 = x[mask_array_50744021]
	
	jac[:,0]= exp_40623151
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_40623151
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_40623151
	jac[:,3]= exp_64133599
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_64133599
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_64133599
	jac[:,6]= exp_57725979
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_57725979
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_57725979
	jac[mask_array_50744021,9]= 1
	
	
	return jac