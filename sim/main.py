import sys
import state as st
import rocket as ro
import components as co

def main():
	initial_state = {
		"xpos": 0,
		"ypos": 0,
		"zpos": 0,
		"xvel": 0,
		"yvel": 0,
		"zvel": 0,
		"xacc": 0,
		"yacc": 0,
		"zacc": 0,
		"theta_roll": 0,
		"theta_pitch": 0,
		"theta_yaw": 0,
		"omega_roll": 0,
		"omega_pitch": 0,
		"omega_yaw": 0,
		"alpha_roll": 0,
		"alpha_pitch": 0,
		"alpha_yaw": 0,
		"time": 0,
	}
	vehicle_state = st.State(initial_state)
	
	# TODO add some sort of environment class
	
	# make the rocket object for position referencing
	vehicle = ro.Rocket(vehicle_state)
	# generate the structural components
	structure = co.Component(10, [.1, 0, 0], "structure")
	structure1 = co.Component(10, [.1, 0, 0], "structure1")
	structure2 = co.Component(10, [.1, 0, 0], "structure2")
	structure3 = co.Component(10, [.1, 0, 0], "structure3")
	vehicle.add_components(structure, structure1, structure2, structure3)
	sensor1 = co.Sensor('accel', [0, 10], structure2)
	vehicle.add_components(sensor1)
	print(vehicle.get_components())
	print(vehicle.get_state()['xpos'])
	

if __name__ == "__main__":
	main()

