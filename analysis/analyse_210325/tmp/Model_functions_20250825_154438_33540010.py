
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
	mask_array_81261984 = (x > 760.4376090259999) & (x < 774.4800570259999);sub_x_81261984 = x[mask_array_81261984];sum[mask_array_81261984] += arg_12
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9,arg_10,arg_11,arg_12):
	l=13
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_84348365 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_70658945 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_40412908 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	exp_40186529 = np.exp(-(x-arg_10)**2/(2*arg_11**2))
	mask_array_10640915 = (x > 760.4376090259999) & (x < 774.4800570259999);sub_x_10640915 = x[mask_array_10640915]
	
	jac[:,0]= exp_84348365
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_84348365
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_84348365
	jac[:,3]= exp_70658945
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_70658945
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_70658945
	jac[:,6]= exp_40412908
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_40412908
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_40412908
	jac[:,9]= exp_40186529
	jac[:,10]= arg_9*(x-arg_10)   /(arg_11**2) * exp_40186529
	jac[:,11]= arg_9*(x-arg_10)**2/(arg_11**3) * exp_40186529
	jac[mask_array_10640915,12]= 1
	
	
	return jac