import numpy as np

class Component():
	''' 
	A part of the rocket with two properties: a writable mass and fixed center of gravity.
	
	Mass is simply the mass of the component in [kg]
	
	Position is the position of the component w.r.t. the center of the rocket
	in the body frame in [m]
	'''
	
	def __init__(self, mass, position, name):
		self.mass =  mass
		self.position = np.array(position)
		self.name = name
		
	def get_mass(self):
		return(self.mass)
	
	def get_pos(self):
		return(self.position)
		
	def get_name(self):
		return(self.name)
		
#class Structural(Component):
#class CenteringRing(Structural):
#class Airframe(Structural):
#class Bulkhead(Structural):
#class MiscMass(Structural):
#class LandingGear(Structural):

#class AeroSurface(Component):
#class Fin(AeroSurface):

#class Motor(Component):

#class Actuator(Component):

#class Electrical(Component):

class Sensor():
	'''
	A sensor is a type of component that reads the state data
	
	A sensor has some type of noise as well that is defined in init
	
	The sensor is also affected by its position, so this must be 
	accounted for in the dynamics math
	'''
	
	def __init__(self, measure_type, measure_range, parent_component = None, sensor_noise = 0):
		self.measure_type = measure_type
		self.measure_range = measure_range
		self.parent_component = parent_component
		self.name = parent_component.get_name() + measure_type
		self.sensor_noise = sensor_noise
		
	def get_pos(self):
		if (self.parent_component):
			return(self.parent_component.get_pos())
		
	def get_value(self):
		return(0)
