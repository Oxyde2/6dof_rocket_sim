'''Program for simulating rocket flight with possible controller implementation'''
import sys

def main():
	initial_state = []
	initial_time = 0
	vehicle_state = state(initial_state, initial_time)
	
	environmental_cond = []
	test_env = environment(environment_cond)
	
	# make the rocket object for position referencing
	vehicle = rocket(vehicle_state)
	# generate the structural components
	structure = create_structural_components()
	
	
	
	pass
	
def create_structural_components():
	airframe = structure(mass, position, 'shape', length, radius)
	landing_gear = structure(mass, position, 'shape', length)
	bulkhead = structure(mass, position, 'shape', length, radius)
	epoxy = structure(mass, position, 'shape')
	centering_ring = structure(mass, position, 'shape', length, radius1, radius2)
	
	return [airframe, landing_gear]

if __name__ == "__main__":
	main()

