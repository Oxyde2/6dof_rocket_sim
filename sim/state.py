from numpy import array
from numpy import iscomplex
from numpy import ndim

class State:

	def __init__(self, initial_conditions, t0 = 0):
		self.state = array(initial_conditions)
		if(t0 < 0 or iscomplex(t0) or ndim(t0) != 0):
			return("t0 must be a natural scalar")
		self.timeStart = t0

