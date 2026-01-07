#kretanje nerelativistickih cestica u aproksimaciji postojanog (u vremenu) dipolnog magnetnog polja planete Zemlje

print('Izabrati proton čije se kretanje ispituje? (1) E = 10MeV; r = 2.5*R_z ili (2) E = 250MeV; r = 4*R_z. (Uneti samo broj)')
proton = int(input())
if proton !=1 and proton !=2:
    print('Neispravan unos.')
    exit()

##################################
# Ucitavanje neophodnih biblioteka
##################################

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#############################
# Ulazni podaci za simulaciju
#############################

dt = 0.0001 #korak integracije - modifikovati u zavisnosti od situacije, odnosno pocetnih uslova
ts = 0.5 #trajanje simulacije
Nkoraka = int(ts/dt) #broj koraka
t = np.zeros(Nkoraka)

##########################
# Definisanje promenljivih
##########################

c = 299792458.0 #[m/s]
RZ = 6378137.0 #[m]
m = 1.6726219e-27 #[kg]
m_e = 9.10938356e-31 #[kg]
q = 1.6021766210e-19 #[C]

mag_osa = np.deg2rad(11.7) #11.7 stepeni je ugao koji zaklapa magnetna osa sa osom rotacije Zemlje, pretvaramo u radijane

sinphi = np.sin(mag_osa) 
cosphi = np.cos(mag_osa)


#################
# Inicijalizacije
#################

rvek = np.zeros((len(t), 3))
vvek = np.zeros((len(t), 3))



def BP(R): #aproksimacija dipolnog magnetnog polja planete Zemlje
    pom = (R[0]**2.0 + R[1]**2.0 + R[2]**2.0)**2.5
    BPx = -7.965626e15*((3.0*R[0]*R[2]*cosphi) + (3.0*R[0]*R[1]*sinphi))/pom
    BPy = -7.965626e15*((3.0*R[1]*R[2]*cosphi) + (2.0*sinphi*(R[1]**2.0)) - (sinphi*(R[0]**2.0)) - (sinphi*(R[2]**2.0)))/pom
    BPz = -7.965626e15*((2.0*cosphi*(R[2]**2.0)) - (cosphi*(R[0]**2.0)) - (cosphi*(R[1]**2.0)) + (3.0*R[2]*R[1]*sinphi))/pom  
    BP = np.array([BPx, BPy, BPz])
    return BP 


if proton == 1:
	rvek[0, :] = np.array([2.5, 0.0, 0.0])*RZ
	vvek[0, :] = np.array([0.0, 0.145*np.sin(mag_osa),0.145*np.cos(mag_osa)])*0.5*c

if proton == 2:
	rvek[0, :] = np.array([4.0, 0.0, 0.0])*RZ
	vvek[0, :] = np.array([0.0, 0.616*np.sin(mag_osa),0.616*np.cos(mag_osa)])*0.866*c



###############
# Racun putanje
###############


for i in range(1, Nkoraka): #RK4 algoritam
    rk1 = rvek[i-1, :]
    vk1 = vvek[i-1, :]
    ak1 = (q/m)*np.cross(vk1, BP(rk1))
    rk2 = rvek[i-1, :] + (0.5*vk1*dt)
    vk2 = vvek[i-1, :] + (0.5*ak1*dt)
    ak2 = (q/m)*np.cross(vk2, BP(rk2))
    rk3 = rvek[i-1, :] + (0.5*vk2*dt)
    vk3 = vvek[i-1, :] + (0.5*ak2*dt)
    ak3 = (q/m)*np.cross(vk3, BP(rk3))
    rk4 = rvek[i-1, :] + (vk3*dt)
    vk4 = vvek[i-1, :] + (ak3*dt)
    ak4 = (q/m)*np.cross(vk4, BP(rk4))
    rvek[i] = rvek[i-1, :] + (dt/6.0)*(vk1 + (2.0*vk2) + (2.0*vk3) + vk4)
    vvek[i] = vvek[i-1, :] + (dt/6.0)*(ak1 + (2.0*ak2) + (2.0*ak3) + ak4)
    t[i] = dt*i
    print(i)


###################################
# Graficko predstavljanje rezultata
###################################


fig = plt.figure() #graficki prikaz
ax = fig.add_subplot(111, projection='3d')

ax.grid(False)
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j] #crtanje grube skice planete Zemlje kao lopte
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color = "seagreen")
plt.xlabel("$x[R_T]$")
plt.ylabel("$y[R_T]$")
ax.set_zlabel("$z[R_T]$")
plt.axis('on')
#ax.set_xlim3d(-8, 8) #modifikovati po potrebi
#ax.set_ylim3d(-8, 8)
#ax.set_zlim3d(-8, 8)
plt.plot(rvek[:, 0]/RZ, rvek[:, 1]/RZ, rvek[:, 2]/RZ, color = 'orangered')
plt.show()
