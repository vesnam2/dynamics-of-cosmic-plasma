###################################
# Ucitavanje neophodnih biblioteka
##################################

import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
import PVREDNOSTI, DEFPOLJA # U istom direktorijumu kao i glavni program

#############################
# Ulazni podaci za simulaciju
#############################

N = 1 # Broj cestica u razmatranoj plazmi - npr. jedna cestica

T_sim = 3000 # TRAJANJE SIMULACIJE [s] (Za elektron T_sim = 1, za proton i alfa česticu T_sim=3000)
dt = 0.1 # VREMENSKI KORAK (pozeljno da bude mali u odnosu na jedan ziro-period 2pim/qB) Za elektron dt=0.001, za proton i alfa česticu 0.1

##########################
# Definisanje promenljivih
##########################


q = np.zeros(N)
m = np.zeros(N)
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)
vz = np.zeros(N)

EPx = 0.0
EPy = 0.0
EPz = 0.0
BPx = 0.0
BPy = 0.0
BPz = 0.0 
pomx = np.zeros(N)
pomy = np.zeros(N)
pomz = np.zeros(N)

Nkoraka = round(T_sim/dt) #Jer se dobije broj u formatu .0 i onda ne prepoznaje kao broj u arange fji
time = np.arange(0, T_sim, dt)

Rx = np.zeros(Nkoraka) #Prazni nizovi za čuvanje koordinata čestice
Ry = np.zeros(Nkoraka)
Rz = np.zeros(Nkoraka)
Tk = np.zeros(Nkoraka) #Kinetička energija


#################
# Inicijalizacije
#################

t = 0.0
 
q, m, x, y, z, vx, vy, vz = PVREDNOSTI.puslovi(N, np) #u zavisnosti od tipa čestica se menja

BPx, BPy, BPz, EPx, EPy, EPz = DEFPOLJA.const_B(x, y, z, t) 


###############
# Racun putanje
###############



i = 1

while t < (T_sim - dt):
	
	t = t + dt	
	
	pomx = vx + ((q*dt*0.5/m)*(EPx + (vy*BPz) - (BPy*vz)))
	pomy = vy + ((q*dt*0.5/m)*(EPy + (vz*BPx) - (BPz*vx)))
	pomz = vz + ((q*dt*0.5/m)*(EPz + (vx*BPy) - (BPx*vy)))

	x = x + (pomx*dt)
	y = y + (pomy*dt)
	z = z + (pomz*dt)

	BPx, BPy, BPz, EPx, EPy, EPz = DEFPOLJA.const_B(x, y, z, t)

	pomx = pomx + ((q*dt*0.5/m)*EPx)
	pomy = pomy + ((q*dt*0.5/m)*EPy)
	pomz = pomz + ((q*dt*0.5/m)*EPz)
	
	vx = ((1.0 + (((q*dt*0.5/m)**2.0)*(BPx**2.0 + BPy**2.0 + BPz**2.0)))**(-1.0))*(pomx + ((q*dt*0.5/m)*(pomy*BPz - pomz*BPy)) + (((q*dt*0.5/m)**2.0)*BPx*(pomx*BPx + pomy*BPy + pomz*BPz)))

	vy = ((1.0 + (((q*dt*0.5/m)**2.0)*(BPx**2.0 + BPy**2.0 + BPz**2.0)))**(-1.0))*(pomy + ((q*dt*0.5/m)*(pomz*BPx - pomx*BPz)) + (((q*dt*0.5/m)**2.0)*BPy*(pomx*BPx + pomy*BPy + pomz*BPz))) 

	vz = ((1.0 + (((q*dt*0.5/m)**2.0)*(BPx**2.0 + BPy**2.0 + BPz**2.0)))**(-1.0))*(pomz + ((q*dt*0.5/m)*(pomx*BPy - pomy*BPx)) + (((q*dt*0.5/m)**2.0)*BPz*(pomx*BPx + pomy*BPy + pomz*BPz)))

	Rx[i-1] = x
	Ry[i-1] = y
	Rz[i-1] = z

	Tk[i-1] = m*0.5*(vx**2.0 + vy**2.0 + vz**2.0)
	
	i = i+1


#Iz nekog razloga je poslednja tačka ista kao i prva, verovatno nešto kod while petlje tako da brišem poslednju tačku
Rx = Rx[:-1]
Ry = Ry[:-1]
Rz = Rz[:-1]
Tk = Tk[:-1]
time = time[:-1]



kinetickainit = Tk[0] #početna kinetička energija
kinetickafin = Tk[-1] #finalna kinetička energija

print((kinetickainit - kinetickafin)/kinetickainit)


###################################
# Graficko predstavljanje rezultata
###################################


#Plotovanje putanje
fig = plt.figure() 
ax = Axes3D(fig) 

plot_geeks = ax.plot(Rx, Ry, Rz, color='slateblue') 

ax.set_title('Putanja elektrona u homogenom magnetnom polju') 
ax.set_xlabel('x') 
ax.set_ylabel('y') 
ax.set_zlabel('z') 
plt.savefig('PutanjaB5.png')
plt.show()


#Plotovanje kinetičke energije
plt.plot(time, Tk, color='slateblue')
plt.title('Promena kinetičke energije elektrona u homogenom magnetnom polju')
plt.xlabel('t [s]')
plt.ylabel('Kinetička energija T [J]')
plt.savefig('KinetickaB5.png')
plt.show()