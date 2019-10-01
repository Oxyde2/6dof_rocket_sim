from numpy import array
from numpy import iscomplex
from numpy import ndim

class State:
'''
the state is the current relevant condition of an object

the state is a dictionary so that sensors can read it easier
'''

	def __init__(self, initial_conditions, t0 = 0):
		self.state = initial_conditions
		if(t0 < 0 or iscomplex(t0) or ndim(t0) != 0):
			return("t0 must be a natural scalar")
		self.timeStart = t0

