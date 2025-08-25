
# Function definition
import numpy as np
from numba import jit

def model_function(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6):
	l=7
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	sum = np.zeros((len(x), ),dtype=np.float64)
	sum+=arg_0*np.exp(-(x-arg_1)**2/(2*arg_2**2))
	sum+=arg_3*np.exp(-(x-arg_4)**2/(2*arg_5**2))
	mask_array_1635629 = (x > 777.9906690260001) & (x < 782.8665190260002);sub_x_1635629 = x[mask_array_1635629];sum[mask_array_1635629] += arg_6
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6):
	l=7
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_55111405 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_86360677 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	mask_array_9214376 = (x > 777.9906690260001) & (x < 782.8665190260002);sub_x_9214376 = x[mask_array_9214376]
	
	jac[:,0]= exp_55111405
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_55111405
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_55111405
	jac[:,3]= exp_86360677
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_86360677
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_86360677
	jac[mask_array_9214376,6]= 1
	
	
	return jac