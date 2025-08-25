
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
	mask_array_80963043 = (x > 984.5796120610001) & (x < 995.9347520609999);sub_x_80963043 = x[mask_array_80963043];sum[mask_array_80963043] += arg_9
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9):
	l=10
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_83441539 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_80855360 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_56820347 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	mask_array_56368313 = (x > 984.5796120610001) & (x < 995.9347520609999);sub_x_56368313 = x[mask_array_56368313]
	
	jac[:,0]= exp_83441539
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_83441539
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_83441539
	jac[:,3]= exp_80855360
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_80855360
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_80855360
	jac[:,6]= exp_56820347
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_56820347
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_56820347
	jac[mask_array_56368313,9]= 1
	
	
	return jac