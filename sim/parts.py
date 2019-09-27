import numpy as np

class Component():
	''' A part of the rocket with two properties: a writable mass and fixed center of gravity.
	
	Mass is simply the mass of the component in [kg]
	
	Position is the position of the component w.r.t. the bottom of the rocket
	in the body frame in [m]
	
	'''
	
	def __init__(self, mass, position):
		self.mass =  mass
		self.position = np.array(position)
		
	
class Structural(Component):
class Fin(Component):
class Motor(Component):
class Actuator(Component):
class Electrical(Component):