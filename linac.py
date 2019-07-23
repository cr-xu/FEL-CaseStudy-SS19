import numpy as np
from scipy import constants
import matplotlib.pyplot as plt

Ean = 140e6#eV
c = constants.speed_of_light
me = constants.electron_mass
hbar = constants.hbar
e = constants.e
def lorentzfactor(E):
    return E/E0

def linac_energy(n,U0,f,phi):#n-number of cavity, U0-Spannung, f- RF frequenz  
    lamb = c/f
    Lc= lamb/2
    l = Lc*n
    phi = np.deg2rad(phi)
    E = n*e*U0*np.cos(phi)/(constants.eV*1e9)
    return E,l,Lc

f =1.5e9#Hz
rfphase1 = -40
number1= 1000
U0 = 3e6
linac1 = linac_energy(number1,U0,f,rfphase1)
E1 = linac1[0]
l1 = linac1[1]
E10 = E1+Ean/1e9
print('Lc',linac1[2],'m')
print('----Linac1--------')
print('Energie:',E10,'GeV')
print('Gesamtlaege:',l1,'m')
GadienE1 = E1/l1
print(GadienE1*1e3,'MeV/m')

rfphase2 = -10
number2 =2600
linac2 = linac_energy(number2,U0,f,rfphase2)
E2= linac2[0]
l2 = linac2[1]
E = E10+E2
print('\n')
print('-----linac2--------')
print('Energie:',E,'GeV')
print('Gesamtlaege',l2,'m')
GE = E2/l2
print(GE*1e3,'MeV/m')

#Energy Chirp
def chirp(phi,Ef,f):
    lamb = c/f
    U = Ef-Ean
    return -2*np.pi*U*np.sin(np.deg2rad(phi))/(lamb*Ef)


print((E1*1e9-Ean)/(E1*1e9))
h1 = chirp(rfphase1,E1*1e9,f)
print('\n')
print('h1:',h1)
print('R56_1',(-1/h1)*1000,'mm')


h=-2*np.pi*np.sin(np.deg2rad(rfphase1))/(c/f)
print((-1/h)*1000)
