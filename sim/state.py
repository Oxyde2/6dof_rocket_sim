from numpy import array
from numpy import iscomplex
from numpy import ndim

class State:
	'''
	the state is the current relevant condition of an object

	the state is a dictionary so that sensors can read it easier
	'''

	def __init__(self, initial_conditions):
		if(
		initial_conditions["time"] < 0 or 
		iscomplex(initial_conditions["time"]) or 
		ndim(initial_conditions["time"]) != 0
		):
			return("t0 must be a natural scalar")
		self.state = initial_conditions
		
	def get_state(self):
		return self.state
		

