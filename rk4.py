def rk4(tStep, xn, yn):
	k1 = tStep*xn
	k2 = tStep*(xn + k1/2)
	k3 = tStep*(xn + k2/2)
	k4 = tStep*(xn + k3)
	return (yn + (1/6)*(k1 + 2*k2 + 2*k3 + k4)) 