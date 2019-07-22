import numpy as np
from scipy import constants
import matplotlib.pyplot as plt

Ean = 140e6#eV
c = constants.speed_of_light
me = constants.electron_mass
hbar = constants.hbar
e = constants.e
E0 = me*c**2/constants.eV
print(e)
def lorentzfactor(E):
    return E/E0


def linac_energy(n,U0,f,phi):#n-number of cavity, U0-Spannung, f- RF frequenz  
    E,l = [],[]
    T = 1/f
    phi = np.deg2rad(phi)
    for i in np.arange(1,n,1):
        Ei = i*e*U0*np.cos(phi)
        li = np.sqrt(Ei/(2*me))/f
        E.append((Ei/constants.eV)/1e9)
        l.append(li)
    return E,l

result = linac_energy(115,2e6,0.9e9,-40)
E1 = result[0]
l1 = result[1]
sumE = sum(E1)+Ean/1e9
suml = sum(l1)
GadienE = sumE/suml
print(sumE)
print(suml)
print(GadienE*1e3,'MeV/m')

#Energy Chirp
def chirp(phi,Ef,f,U):
    lamb = c/f
    eU = e*U/constants.eV
    return -2*np.pi*eU*np.sin(phi)/(lamb*Ef)

print(chirp(-40,10e9,0.9e9,2e6))    
