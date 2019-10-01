import numpy as np

class Component():
	''' 
	A part of the rocket with two properties: a writable mass and fixed center of gravity.
	
	Mass is simply the mass of the component in [kg]
	
	Position is the position of the component w.r.t. the bottom of the rocket
	in the body frame in [m]
	'''
	
	def __init__(self, mass, position):
		self.mass =  mass
		self.position = np.array(position)
		
	def get_mass():
		return(self.mass)
	
	def get_pos():
		return(self.position)
		
class Structural(Component):
class CenteringRing(Structural):
class Airframe(Structural):
class Bulkhead(Structural):
class MiscMass(Structural):
class LandingGear(Structural):

class AeroSurface(Component):
class Fin(AeroSurface):

class Motor(Component):

class Actuator(Component):

class Electrical(Component):

class Sensor():
	'''
	A sensor is a type of component that reads the state data
	
	A sensor has some type of noise as well that is defined in init
	
	The sensor is also affected by its position, so this must be 
	accounted for in the dynamics math
	'''
	
	def __init__(self, measurement_type, sensor_noise, )