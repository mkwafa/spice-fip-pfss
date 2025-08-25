
# Function definition
import numpy as np
from numba import jit

def model_function(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6):
	l=7
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	sum = np.zeros((len(x), ),dtype=np.float64)
	sum+=arg_0*np.exp(-(x-arg_1)**2/(2*arg_2**2))
	sum+=arg_3*np.exp(-(x-arg_4)**2/(2*arg_5**2))
	mask_array_97531432 = (x > 777.9906690260001) & (x < 782.8665190260002);sub_x_97531432 = x[mask_array_97531432];sum[mask_array_97531432] += arg_6
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6):
	l=7
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_19264923 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_77363063 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	mask_array_2968284 = (x > 777.9906690260001) & (x < 782.8665190260002);sub_x_2968284 = x[mask_array_2968284]
	
	jac[:,0]= exp_19264923
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_19264923
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_19264923
	jac[:,3]= exp_77363063
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_77363063
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_77363063
	jac[mask_array_2968284,6]= 1
	
	
	return jac