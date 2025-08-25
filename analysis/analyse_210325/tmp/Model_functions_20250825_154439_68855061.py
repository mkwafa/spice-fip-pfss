
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
	mask_array_52019265 = (x > 760.4376090259999) & (x < 774.4800570259999);sub_x_52019265 = x[mask_array_52019265];sum[mask_array_52019265] += arg_12
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9,arg_10,arg_11,arg_12):
	l=13
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_69266492 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_93685255 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_14335112 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	exp_82540194 = np.exp(-(x-arg_10)**2/(2*arg_11**2))
	mask_array_89069918 = (x > 760.4376090259999) & (x < 774.4800570259999);sub_x_89069918 = x[mask_array_89069918]
	
	jac[:,0]= exp_69266492
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_69266492
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_69266492
	jac[:,3]= exp_93685255
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_93685255
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_93685255
	jac[:,6]= exp_14335112
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_14335112
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_14335112
	jac[:,9]= exp_82540194
	jac[:,10]= arg_9*(x-arg_10)   /(arg_11**2) * exp_82540194
	jac[:,11]= arg_9*(x-arg_10)**2/(arg_11**3) * exp_82540194
	jac[mask_array_89069918,12]= 1
	
	
	return jac