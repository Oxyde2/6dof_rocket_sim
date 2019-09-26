from numpy import array
from numpy import any
from numpy import iscomplex
from numpy import ndim

def eulerStep(tStep, xn, yn):
	if (ndim(tStep) != 0):
		return('tStep is not a scalar')
	if (iscomplex(tStep)):
		return('tStep is not real')
	if (tStep < 0):
		return('tStep is < 0')
	if (tStep > .005):
		print('be careful with large time steps')
		
	xn = array(xn)
	yn = array(yn)
	
	if (xn.size == 0):
		return('xn cannot be empty')
	if(any(xn) == None):
		return('xn cannot have any None')
	if (yn.size == 0):
		return('yn cannot be empty')
	if(any(yn) == None):
		return('yn cannot have any None')
	if(iscomplex(xn).any()):
		return('xn cannot have any imaginary numbers')
	if(iscomplex(yn).any()):
		return('yn cannot have any imaginary numbers')
	
	ynp1 = yn + tStep*xn
	
	return  ynp1
