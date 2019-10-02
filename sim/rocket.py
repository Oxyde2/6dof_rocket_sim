import numpy as np

class Rocket():
	'''
	This class is meant to act as a backbone to add components

	Its state is all the variables we care about

	Components can be assigned to the rocket as well
	'''

	def __init__(self, initial_state, components = {}):
		self.state = initial_state
		self.components = components
		
	def get_state(self):
		return self.state.get_state()
	
	def update_state(self, new_state):
		self.state = new_state
		
	def add_components(self,*args):
		for component in args:
			key = component.name
			self.components[key] = component
	
	def get_components(self):
		return self.components
		
	def get_total_mass(self):
		total_mass = 0
		for component in self.components.values:
			total_mass += component.get_mass()
		return total_mass
		
		
	


