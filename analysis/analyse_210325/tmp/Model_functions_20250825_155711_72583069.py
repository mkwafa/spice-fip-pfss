
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
	mask_array_66586259 = (x > 760.4376090259999) & (x < 774.4800570259999);sub_x_66586259 = x[mask_array_66586259];sum[mask_array_66586259] += arg_12
	return sum





# Jacobian definition
import numpy as np
from numba import jit

def model_jacobian(x,arg_0,arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,arg_9,arg_10,arg_11,arg_12):
	l=13
	if isinstance(x,float):x = np.array([x],dtype=np.float64)
	jac = np.zeros((len(x),l),dtype=np.float64)
	exp_57750530 = np.exp(-(x-arg_1)**2/(2*arg_2**2))
	exp_86870874 = np.exp(-(x-arg_4)**2/(2*arg_5**2))
	exp_16363507 = np.exp(-(x-arg_7)**2/(2*arg_8**2))
	exp_37291554 = np.exp(-(x-arg_10)**2/(2*arg_11**2))
	mask_array_67954191 = (x > 760.4376090259999) & (x < 774.4800570259999);sub_x_67954191 = x[mask_array_67954191]
	
	jac[:,0]= exp_57750530
	jac[:,1]= arg_0*(x-arg_1)   /(arg_2**2) * exp_57750530
	jac[:,2]= arg_0*(x-arg_1)**2/(arg_2**3) * exp_57750530
	jac[:,3]= exp_86870874
	jac[:,4]= arg_3*(x-arg_4)   /(arg_5**2) * exp_86870874
	jac[:,5]= arg_3*(x-arg_4)**2/(arg_5**3) * exp_86870874
	jac[:,6]= exp_16363507
	jac[:,7]= arg_6*(x-arg_7)   /(arg_8**2) * exp_16363507
	jac[:,8]= arg_6*(x-arg_7)**2/(arg_8**3) * exp_16363507
	jac[:,9]= exp_37291554
	jac[:,10]= arg_9*(x-arg_10)   /(arg_11**2) * exp_37291554
	jac[:,11]= arg_9*(x-arg_10)**2/(arg_11**3) * exp_37291554
	jac[mask_array_67954191,12]= 1
	
	
	return jac