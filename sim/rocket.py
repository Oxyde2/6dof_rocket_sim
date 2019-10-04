import numpy as np
import geometry as geo

class Rocket():
	'''
	This class is meant to act as a backbone to add components

	Its state is all the variables we care about

	Components can be assigned to the rocket as well
	'''

	def __init__(self, initial_state, mass = 0, inertia = 0, components = {}):
		self.state = initial_state
		self.components = components
		if not components:
			self.mass = mass
			self.inertia_tensor = inertia
		else:
			calculate_mass()
			calculate_inertia()
		
	def get_state(self):
		return self.state.get_state()
	
	def update_state(self, new_state):
		self.state = new_state
		
	def add_components(self,*args):
		# add components to the dictionary, then find the new total mass
		for component in args:
			key = component.name
			self.components[key] = component
		self.calculate_mass()
		self.calculate_inertia_tensor()
	
	#TODO write a method for removing components to test breakage
	
	def get_components(self):
		return self.components
		
	def calculate_mass(self):
		total_mass = 0
		if not self.components:
			self.mass = total_mass
		else:
			component_list = self.components.values()
			for component in component_list:
				total_mass += component.get_mass()
		self.mass = total_mass
		
	def get_mass(self):
		return self.mass

	# TODO implement an orientation adjustemnt
	def calculate_inertia_tensor(self):
		inertia_tensor = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
		if not self.components:
			self.inertia_tensor = inertia_tensor
		else:
			component_list = self.components.values()
			for component in component_list:
				#TODO complete the other components of the inertia tensor matrix
				#component_inertia_tensor = component.get_inertia_tensor()
				rotated_inertia_tensor = geo.rotate_matrix(component.get_inertia_tensor(),component.orientation)
				ixx_component = component.get_inertia_tensor()[0,0]
				ixx_distance = component.get_mass()*(component.get_pos()[1]**2 + component.get_pos()[2]**2)
				inertia_tensor[0,0] += (ixx_component + ixx_distance)
				
		self.inertia_tensor = inertia_tensor
		
	def get_inertia_tensor(self):
		return self.inertia_tensor
	
		
	
		
		
	


