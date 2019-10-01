import sys

def main():
	initial_state = {
		"xpos": 30,
		"ypos": 0,
		"zpos": 0,
		"xvel": 0,
		"yvel": 0,
		"zvel": 0,
		"theta_roll": 0,
		"theta_pitch": 0,
		"theta_yaw": 0,
		"omega_roll": 0,
		"omega_pitch": 0,
		"omega_yaw": 0,
		"time": 0,
	}
	
	vehicle_state = State(initial_state)
	
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
	
def setup_state():
	initial_state = []
	initial_time = 0
	vehicle_state = state(initial_state, initial_time)

if __name__ == "__main__":
	main()

