from numpy import array
from numpy import iscomplex
from numpy import ndim

class State:
'''
the state is the current relevant condition of an object

the state is a dictionary so that sensors can read it easier
'''

	def __init__(self, initial_conditions):
		self.state = initial_conditions
		if(state["time"] < 0 or iscomplex(state["time"]) or ndim(state["time"]) != 0):
			return("t0 must be a natural scalar")

