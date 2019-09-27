import math
import numpy as np
import sympy as sy


# ENVIRONMENT
# gravitational acceleration [m/s^2]
g = 9.81
# air density [kg/m^3]
rho = 1.225
# noise terms
windxdd = 0
windydd = 0
thRollWinddd = -windydd*.2
thPitchWinddd = windxdd*.2


# ROCKET STRUCTURE
# individual inertia elements []
Ixx = 1
Iyy = 1
Izz = 1
# simplified inertia tensor makes dynamics easier
I = np.array([[Ixx, 0, 0], [0, Iyy, 0], [0, 0, Izz]])
# total mass [kg]
mRocket = .5
# total length [m]
l = .5
# z location along rocket of center of gravity defined from bottom (unchanging for now) [m]
zcg = .2
# drag coefficient of the bottom area of the rocket per wikipedia (https://en.wikipedia.org/wiki/Drag_coefficient)
cd = .82
# rocket diameter [m]
d = .03
# rocket bottom and top areas [m^2]
atb = math.pi*(.5*d)**2


# ROCKET ACTUATORS
# maximum thrust produced by the propellers [N]
maxPropThrust = 1
# thrust from the rocket motor [N]
motorThrust = 100
# motor burn time [s]
motorBurnTime = 5


# EQUATIONS OF MOTION SYMBOLICS
# location [m]
x, y, z = sy.symbols('x y z')
# velocity [m/s]
xd, yd, zd = sy.symbols('xd yd zd')
# orientation [rad]
thRoll, thPitch, thYaw = sy.symbols('thRoll thPitch thYaw')
# angular rates [rad]
thRolld, thPitchd, thYawd = sy.symbols('thRolld thPitchd thYawd')
# inputs [N]
fthrust, fxprop, fyprop = sy.symbols('fthrust fxprop fyprop')
# other things (drag on bottom, moments)
fdrag = .5*rho*cd*atb*xd**2
Mx = fyprop*(l-zcg)
My = fxprop*(l-zcg)
Mz = 0


# POSITION EQUATIONS OF MOTION [BODY FRAME]
# x-acceleration
xdd = fxprop/mRocket
# y-acceleration
ydd = fyprop/mRocket
# z-acceleration
zdd = (fthrust + fdrag)/mRocket
# make it a vertical array
xyzEOMsBody = sy.Matrix([xdd, ydd, zdd])


# POSITION EQUATIONS OF MOTION [INERTIAL FRAME]
# define individual rotation matrices (maybe change to a separate quaternion operator later)
rotRoll = sy.Matrix([[1, 0, 0],[0, sy.cos(thRoll), -sy.sin(thRoll)],[0, sy.sin(thRoll), sy.cos(thRoll)]])
rotPitch = sy.Matrix([[sy.cos(thPitch), 0, sy.sin(thPitch)],[0, 1, 0],[-sy.sin(thPitch), 0, sy.cos(thPitch)]])
rotYaw = sy.Matrix([[sy.cos(thYaw), -sy.sin(thYaw), 0],[sy.sin(thYaw), sy.cos(thYaw), 0], [0, 0, 1]])
RotBtoI = rotYaw.multiply(rotPitch.multiply(rotRoll))
# rotate the whole vector and add gravity to get into inertial frame
xyzEOMsInertial = sy.Matrix([0,0,-g]) + RotBtoI.multiply(xyzEOMsBody)


# ORIENTATION EQUATIONS OF MOTION [INERTIAL FRAME]
# roll-angular acceleration
thRolldd = (Mx + (I[1,1]-I[2,2])*thPitchd*thYawd)/I[0,0] + thRollWinddd
# pitch-angular acceleration
thPitchdd = (My + (I[2,2]-I[0,0])*thRolld*thYawd)/I[1,1] + thPitchWinddd
# yaw-angular acceleration
thYawdd = (Mz + (I[0,0]-I[1,1])*thPitchd*thRolld)/I[2,2] 
# stack into a vector
yprEOMsInertial = sy.Matrix([thYawdd, thPitchdd, thRolldd])

