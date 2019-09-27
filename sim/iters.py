import numpy as np

def euler_step(tStep, xn, yn):
	if (np.ndim(tStep) != 0):
		return('tStep is not a scalar')
	if (np.iscomplex(tStep)):
		return('tStep is not real')
	if (tStep < 0):
		return('tStep is < 0')
	if (tStep > .005):
		print('be careful with large time steps')
		
	xn = np.array(xn)
	yn = np.array(yn)
	
	if (xn.size == 0):
		return('xn cannot be empty')
	if(np.any(xn) == None):
		return('xn cannot have any None')
	if (yn.size == 0):
		return('yn cannot be empty')
	if(np.any(yn) == None):
		return('yn cannot have any None')
	if(np.iscomplex(xn).any()):
		return('xn cannot have any imaginary numbers')
	if(np.iscomplex(yn).any()):
		return('yn cannot have any imaginary numbers')
	
	ynp1 = yn + tStep*xn
	
	return  ynp1