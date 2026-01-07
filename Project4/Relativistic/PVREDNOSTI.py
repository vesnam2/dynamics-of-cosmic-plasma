###########################
# Zadavanje pocetnih uslova
###########################

def puslovi(N, np, proton):
	
	import random
	
	########################################
	# Ulazni podaci (fizicke karakteristike)
	########################################

	m_e = 9.10938356e-31 # Masa elektrona [kg]
	m_p = 1.6726219e-27 # Masa protona [kg]
	qelem = 1.6021766210e-19 # Elementarno naelektrisanje [C]
	c = 299792458.0 # Brzina svetlosti u vakuumu [m/s]

	q = np.zeros(N)
	m = np.zeros(N)
	x = np.zeros(N)
	y = np.zeros(N)
	z = np.zeros(N)
	vx = np.zeros(N)
	vy = np.zeros(N)
	vz = np.zeros(N)
	
	for i in range(0,N):

		q[i] = 1.0*qelem
		m[i] = 1.0*m_p 
		
		if proton == 1:
			x[i] = 2.5*6378137.0
			y[i] = 0.0
			z[i] = 0.0
			vx[i] = 0.0
			vy[i] = 0.145*0.5*c
			vz[i] = 0.145*0.866*c
		elif proton == 2:
			x[i] = 4.0*6378137.0 
			y[i] = 0.0
			z[i] = 0.0
			vx[i] = 0.0
			vy[i] = 0.616*0.5*c
			vz[i] = 0.616*0.866*c
		
	return q, m, x, y, z, vx, vy, vz
