
# Function definition
import numpy as np
from numba import jit

def model_function(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6):
	l=7
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	sum = np.zeros((len(x), ),dtype=np.float64)
	sum+=arg_0*np.exp(-(x-arg_1)**2/(2*arg_2**2))
	sum+=arg_3*np.exp(-(x-arg_4)**2/(2*arg_5**2))
	mask_array_34850478 = (x > 777.9906690260001) & (x < 782.8665190260002);sub_x_34850478 = x[mask_array_34850478];sum[mask_array_34850478] += arg_6
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6):
	l=7
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_4930910 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_61181238 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	mask_array_51814125 = (x > 777.9906690260001) & (x < 782.8665190260002);sub_x_51814125 = x[mask_array_51814125]
	
	jac[:,0]= exp_4930910
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_4930910
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_4930910
	jac[:,3]= exp_61181238
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_61181238
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_61181238
	jac[mask_array_51814125,6]= 1
	
	
	return jac