
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
	mask_array_60111804 = (x > 782.671485026) & (x < 790.472845026);sub_x_60111804 = x[mask_array_60111804];sum[mask_array_60111804] += arg_9
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9):
	l=10
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_40928727 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_37856020 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_97360785 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	mask_array_10112701 = (x > 782.671485026) & (x < 790.472845026);sub_x_10112701 = x[mask_array_10112701]
	
	jac[:,0]= exp_40928727
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_40928727
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_40928727
	jac[:,3]= exp_37856020
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_37856020
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_37856020
	jac[:,6]= exp_97360785
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_97360785
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_97360785
	jac[mask_array_10112701,9]= 1
	
	
	return jac