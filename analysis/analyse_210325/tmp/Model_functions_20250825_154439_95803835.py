
# Function definition
import numpy as np
from numba import jit

def model_function(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9,arg_10,arg_11,arg_12):
	l=13
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	sum = np.zeros((len(x), ),dtype=np.float64)
	sum+=arg_0*np.exp(-(x-arg_1)**2/(2*arg_2**2))
	sum+=arg_3*np.exp(-(x-arg_4)**2/(2*arg_5**2))
	sum+=arg_6*np.exp(-(x-arg_7)**2/(2*arg_8**2))
	sum+=arg_9*np.exp(-(x-arg_10)**2/(2*arg_11**2))
	mask_array_32477069 = (x > 760.4376090259999) & (x < 774.4800570259999);sub_x_32477069 = x[mask_array_32477069];sum[mask_array_32477069] += arg_12
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9,arg_10,arg_11,arg_12):
	l=13
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_70972873 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_94613057 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_38535716 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	exp_13764590 = np.exp(-(x-arg_10)**2/(2*arg_11**2))
	mask_array_58123982 = (x > 760.4376090259999) & (x < 774.4800570259999);sub_x_58123982 = x[mask_array_58123982]
	
	jac[:,0]= exp_70972873
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_70972873
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_70972873
	jac[:,3]= exp_94613057
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_94613057
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_94613057
	jac[:,6]= exp_38535716
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_38535716
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_38535716
	jac[:,9]= exp_13764590
	jac[:,10]= arg_9*(x-arg_10)   /(arg_11**2) * exp_13764590
	jac[:,11]= arg_9*(x-arg_10)**2/(arg_11**3) * exp_13764590
	jac[mask_array_58123982,12]= 1
	
	
	return jac