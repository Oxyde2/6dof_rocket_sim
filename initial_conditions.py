from sympy import Matrix
class State:

	def __init__(self, pos0, vel0, ori0, ang0, t0 = 0):
		# INITIAL CONDITIONS
		# position [m]
		self.x0 = pos0[0]
		self.y0 = pos0[1]
		self.z0 = pos0[2]
		# velocity [m/s]
		self.xd0 = vel0[0]
		self.yd0 = vel0[1]
		self.zd0 = vel0[2]
		# orientation [rad]
		self.thYaw0 = ori0[0]
		self.thPitch0 = ori0[1]
		self.thRoll0 = ori0[2]
		# angular rates [rad/s]
		self.thYawd0 = ang0[0]
		self.thPitchd0 = ang0[1]
		self.thRolld0 = ang0[2]
		# time of the state
		self.timeStart = t0

pos0 = [1,1,1]
vel0 = [1,1,1]
ori0 = [1,1,1]
ang0 = [1,1,1]

state1 = State(pos0,vel0,ori0,ang0,t0 = 3)
print(state1.timeStart)