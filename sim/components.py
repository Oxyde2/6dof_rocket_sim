import numpy as np

class Component():
	''' 
	A part of the rocket with two properties: a writable mass and fixed center of gravity.
	
	Mass is simply the mass of the component in [kg]
	
	Position is the position of the component w.r.t. the center of the rocket
	in the body frame in [m]
	
	Orientation is the angle the component makes with each axis of the rocket
	defined in [rad] in the positive direction as defined by the right hand rule
	
	I used this site for inertia math: https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-07-dynamics-fall-2009/lecture-notes/MIT16_07F09_Lec26.pdf
	'''
	
	def __init__(self, mass, position, orientation, name):
		self.mass =  mass
		self.position = np.array(position)
		self.name = name
		self.orientation = orientation
		
	def get_mass(self):
		return(self.mass)
	
	def get_pos(self):
		return(self.position)
		
	def get_name(self):
		return(self.name)
		
class Cylinder(Component):
	# TODO do some orientation stuff
	def __init__(self, mass, position, name, radius, height):
		self.mass = mass
		self.position = np.array(position).astype(float)
		self.name = name
		self.radius = radius
		self.height = height
		
		Ixx = (self.mass*self.radius**2)
		Iyy = ((1/12)*self.mass*(6*self.radius**2 + self.height**2))
		Izz = (Iyy)
		
		self.inertia_tensor = np.array([[Ixx, 0, 0], [0, Iyy, 0], [0, 0, Izz]])
	
	def get_inertia_tensor(self):
		return self.inertia_tensor
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
