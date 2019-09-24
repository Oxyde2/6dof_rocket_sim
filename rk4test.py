from rk4 import rk4
import time

ax = -9.81
vn = 0
xn = 30
tStep = .005
tn = 0
tf = 10

def accx(vars):
	return ax + .5*abs(vn)

def vel(vars):
	return vn

while tn < tf:
	vnp1 = rk4(vn, tStep, accx, [])
	xnp1 = rk4(xn, tStep, vel, [])
	tn += tStep
	vn = vnp1
	xn = xnp1
	#print(tn, vn, xn)
