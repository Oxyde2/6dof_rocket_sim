from sympy import Matrix
import math

# STATIC QUANTITIES

#---------# GEOMETRY #---------#

# AIRFRAME
# radius of the rocket [m]
radiusAirframe = .02
# length of the rocket [m]
lengthAirframe = .5
# xy cross sectional area of the cylinder [m^2]
xySecArea = .5*math.pi*(radiusAirframe)**2
# xz or yz cross sectional area of cylinder [m^2]
xzSecArea = 2*radiusAirframe*lengthAirframe
# wrapped area of the cylinder [m^2]
wrapArea = 2*math.pi*radiusAirframe*lengthAirframe

# FINS
# height of fins [m]
heightFin = .05
# root chord of fins [m]
rootChordFin = .08
# tip chord of fins [m]
tipChordFin = .03
# area of individual fin [m^2]
areaFin = .5*(rootChordFin+tipChordFin)*heightFin
# thickness of fins [m]
thicknessFin = .002
# number of fins
numFins = 4
# fin spacing [rad]
finSpacing = Matrix([0, math.pi/4, math.pi/2, 3*math.pi/4])

# PROPELLERS
# radius of a propeller [m]
radiusPropellers = .01
# swept area of a propeller [m^2]
areaProp = .5*math.pi*radiusPropellers


#---------# MASSES #---------#

# AIRFRAME 
# mass of the airframe [kg]
massAirframe = .45
# airframe center of gravity from bottom [m]
cgAirframe = .25

# ELECTRONICS
# mass of the electronics [kg]
massElectronics = .05
# electronics center of gravity from bottom [m]
cgElectronics = .3

# MOTOR
# mass of the motor when full
massMotorFull = .1
# mass of the motor when burned
massMotorEmpty = .03

# center of gravity of the motor is relatively constant
cgMotor = .05

# TOTALS

	
	
#---------# INERTIAS #---------#

# individual inertia elements []

#---------# AERODYNAMICS #---------#

# AIRFRAME 
# drag coefficient of the bottom area of the rocket per wikipedia (https://en.wikipedia.org/wiki/Drag_coefficient)
cdXYCrossArea = .82
# drag coefficient of the side of the rocket 
cdXZCrossArea = .47

# FINS
# drag coefficient of a fin in the XY plane
cdXYFin = .02
# drag coefficient of a fin in the XZ or YZ plane
cdXZFin = 1.9

#---------# ACTUATORS #---------#

# PROPELLERS 
# maximum thrust produced by the propellers [N]
maxPropThrust = 1
 
# MOTOR 
# motor burn time [s]
motorBurnLength = 1
# motor ignition time [s]
motorIgniteTime = 3


# DYNAMICS QUANTITIES

#---------# GEOMETRY #---------#

# AIRFRAME

# FINS

# PROPELLERS

#---------# MASSES #---------#

# AIRFRAME 

# ELECTRONICS

# MOTOR
# mass of the motor is defined by an equation [kg]
def massMotor(time):
	if time < motorIgniteTime:
		massMotor = massMotorFull
	elif time > motorIgniteTime + motorBurnLength:
		massMotor = massMotorEmpty
	else:
		massMotor = massMotorFull-(massMotorFull-massMotorEmpty)*((time-motorIgniteTime)/(motorIgniteTime+motorBurnLength))
	return massMotor

# TOTALS
# mass of the entire rocket
def massRocket(time):
	massRocket = massAirframe + massElectronics + massMotor(time)
	return massRocket
# cg of the entire rocket
def cgRocket(time):
	cgRocket = cgAirframe*massAirframe + cgElectronics*massElectronics + cgMotor*massMotor(time)
	return cgRocket
	
	
#---------# INERTIAS #---------#

# individual inertia elements []
Ixx = 1
Iyy = 1
def Izz(time):
	Izz = .5*massRocket(time)*radiusAirframe**2
	return Izz
# simplified inertia tensor makes dynamics easier
def inertiaTensor(time):
	inertiaTensor = Matrix([[Ixx, 0, 0], [0, Iyy, 0], [0, 0, Izz(time)]])
print(inertiaTensor(.5))
#---------# AERODYNAMICS #---------#

# AIRFRAME 


# FINS


#---------# ACTUATORS #---------#

# PROPELLERS 
 
# MOTOR 
# thrust from the rocket motor [N]
def motorThrust(time):
	if time > motorIgniteTime & time < (motorIgniteTime+motorBurnLength):
		motorThrust = 20
	else:
		motorThrust = 0