""" Rocket Flight Calculator
    Version = 1.0.0
    Autor: Andre Henry
    Date: 5/12/2024

    This Code is to providoe rought flight calcuation data for a Rocket desing. 
    Assumtions in this code:
        *Gravity is constaint
        *Rocket AOA is zero
        *Rocket is stable
"""
__version__ = "1.0.0"

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci
from rocket_config import Motor

plt.ion # Interactive mode in plots

# Gloabals

GRAVITY = -9.81 # m/s^2 change in gravity considered minimal

# Rocket Physcial Perameters
RocketMass0 = 32098/1000 # kg
diameter = 0.155 # m
S = np.pi*(diameter/2)**2  # m^2 Cross sectional area
Cd = 0.36 # Ceffitant of drag
    
# Rocket Motor Perameters
FuelMass = 7512/1000 # kg
ThrustAvg = 3168.0 # F
TotalImpulse = 14041.0 # Ns
ISP = TotalImpulse/(FuelMass*np.abs(GRAVITY))
#ISP = 200 #sec - motor effciency


# Thrust model
def Thrust(t):
    global ThrustAvg, ISP
    if (t < 4.4):
        Fthrust = ThrustAvg
    else:
        Fthrust = 0.0
    ve = ISP * GRAVITY
    mdot = Fthrust/ve
    return Fthrust, mdot


# Simulation Functions
# Aerodynamics 
def AirDensity(altitude):
    # alternate method would be to intepulate with data
    beta = 0.1354/1000.0 # Density Constant - confrim Constant
    rhos = 1.225 # kg/m^3 at sea level
    rho = rhos * np.exp(-beta*altitude)
    return rho




# Differential equation 
def Derivative(state: np.array, t: int, motor: Motor) -> np.array:
    # State vector
    z = state[0]
    zv = state[1]
    mass = state[2]
    
    # Dynamic pressure calc
    rho = AirDensity(z)
    qinf = 0.5 * rho * S * zv**2 *np.sign(zv)
    
    # Forces
    Fgravity = GRAVITY * mass
    Faero = -qinf * Cd
    Fthrust, mdot = motor.fThrust(t)
    
    Fnet = Fgravity + Faero + Fthrust
    za = Fnet/mass
    
    # Stop integratoin when Rocket returns to ground
    if (z < z0):
        statedot = np.array([0, za, mdot])
    else:
        statedot = np.array([zv, za, mdot])

    return statedot


# Simulation 

# Initial conditions
z0 = 0 # m
zv0 = 0 # m/s
za0 = 0 # m/s**2
t = np.linspace(0,63,10000)

n_motor = Motor(FuelMass, ThrustAvg, TotalImpulse)

stateinitial = np.array([z0, zv0, RocketMass0])

# Integratoin of model
stateout = sci.odeint(Derivative, stateinitial, t, args=(n_motor,))

zout = stateout[:,0]
zvout = stateout[:,1]
massout = stateout[:,2]

# Results 
print('\n\n\nResults:')
print(f'Apogee:  {np.max(zout):.2f}')
print(f'Maxium Velocity:  {np.max(zvout):.2f}')
print(f'ISP:  {np.max(ISP):.2f}')
print('\n')


""" 
plt.figure()
plt.plot(t,zout)
plt.title('Altitude')
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.grid()

plt.figure()
plt.plot(t,zvout)
plt.title('Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid()

plt.figure()
plt.plot(t,massout)
plt.title('Mass')
plt.xlabel('Time (s)')
plt.ylabel('mass (kg)')
plt.grid()

plt.show() """

