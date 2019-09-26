from numpy import array

def eulerStep(tStep, xn, yn):
	if (tStep < 0):
		return('tStep is < 0')
	if (tStep > .01):
		print('be careful with large time steps')
		
	xn = array(xn)
	yn = array(yn)
	
	ynp1 = yn + tStep*xn
	
	return  ynp1
	
	
