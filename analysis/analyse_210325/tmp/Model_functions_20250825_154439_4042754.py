
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
	mask_array_72783735 = (x > 984.5796120610001) & (x < 995.9347520609999);sub_x_72783735 = x[mask_array_72783735];sum[mask_array_72783735] += arg_9
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9):
	l=10
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_29072522 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_95787488 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_20586689 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	mask_array_71527268 = (x > 984.5796120610001) & (x < 995.9347520609999);sub_x_71527268 = x[mask_array_71527268]
	
	jac[:,0]= exp_29072522
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_29072522
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_29072522
	jac[:,3]= exp_95787488
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_95787488
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_95787488
	jac[:,6]= exp_20586689
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_20586689
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_20586689
	jac[mask_array_71527268,9]= 1
	
	
	return jac