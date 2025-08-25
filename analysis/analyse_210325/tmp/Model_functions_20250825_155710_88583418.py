
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
	mask_array_39576733 = (x > 984.5796120610001) & (x < 995.9347520609999);sub_x_39576733 = x[mask_array_39576733];sum[mask_array_39576733] += arg_9
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9):
	l=10
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_83073550 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_93133204 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_17528388 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	mask_array_83718248 = (x > 984.5796120610001) & (x < 995.9347520609999);sub_x_83718248 = x[mask_array_83718248]
	
	jac[:,0]= exp_83073550
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_83073550
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_83073550
	jac[:,3]= exp_93133204
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_93133204
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_93133204
	jac[:,6]= exp_17528388
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_17528388
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_17528388
	jac[mask_array_83718248,9]= 1
	
	
	return jac