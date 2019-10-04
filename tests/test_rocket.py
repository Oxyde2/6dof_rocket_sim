import sys
import unittest
import numpy as np
sys.path.append('D:\\6dof_rocket_sim\sim')
import rocket as ro
import components as co

#class TestRocket(unittest.TestCase):
	
land_shark = ro.Rocket({'xpos': 0})
#fin1 = co.Component(10, [0,1,0], 'fin1')
#fin2 = co.Component(10, [0,1,0], 'fin2')
#fin3 = co.Component(10, [0,1,0], 'fin3')
#fin4 = co.Component(10, [0,1,0], 'fin4')
airframe = co.Cylinder(10, [1, 1, 1], 'airframe', .1, 10)
#print(airframe.get_inertia_tensor()[0,0])
#print(airframe.mass*(airframe.get_pos()[1]**2 + airframe.get_pos()[2]**2))
land_shark.add_components(airframe)
#print(land_shark.get_components())
#print(land_shark.get_mass())
np.set_printoptions(precision = 2)
print(type(land_shark.get_inertia_tensor()[0,0]))
print(land_shark.get_inertia_tensor())