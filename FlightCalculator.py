""" Rocket Flight Calculator
    Version = 1.0.0
    Autor: Andre Henry
    Date: 5/12/2024

    This Code is to providoe rought flight calcuation data for a Rocket desing. 
    Assumtions in this code:
        *Gravity is constaint
        *Rocket AOA is zero
        *Rocket is stable and rigid
"""
__version__ = "1.0.0"

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci
from Rocket_Config import RocketConfig, Motor
from Aero_Config import Aero

plt.ion # Interactive mode in plots



# Main differential equation 
def Derivative(state: np.array, t: int, rocket: RocketConfig, motor: Motor) -> np.array:
    """State space equation to be integrated numericaly. 

    Args:
        state (np.array): State Vector [altitude - m, velocity - m/s, mass -kg]
        t (int): Time of current step in integratoin - seconds
        rocket (RocketConfig): Rocketfig class containing perameters/method of rocket
        motor (Motor): Motor class conatin peramters/methods of the motor

    Returns:
        np.array: State array dervivative to be integrated [altitude_dot - m/s, velcoity_dot - m/s**2, mass_dot - kg/s]
    """    
    # State vector
    altitude = state[0]
    velocity = state[1]
    mass = state[2]
    
    GRAVITY = 9.81 # m/s^2 change in gravity considered negligible
    aero = Aero(rocket)
    
   
    # Forces
    f_gravity = GRAVITY * mass
    f_aero = aero.F_aero_drag(velocity, altitude)
    f_thrust, mass_dot = motor.motor_output(t)
    
    f_net = f_thrust - f_aero - f_gravity
    acceleration = f_net/mass
    
    # Stop integratoin when Rocket returns to ground
    if (altitude < z0):
        statedot = np.array([0, acceleration, mass_dot])
    else:
        statedot = np.array([velocity, acceleration, mass_dot])

    return statedot


# Simulation 
# Rocket: Ambition
rocket_mass_0 = 32098/1000 # kilograms
drag_coefficient = 0.36 #cf
diameter = 0.155 # meters
rocket_Ambition = RocketConfig(rocket_mass_0, drag_coefficient, diameter)

# N Motor Perameters
n_fuel_mass = 7512/1000 # kg
n_trust_avg = 3168.0 # Newtons
n_total_impulse = 14041.0 # Newton*seconds
n_total_burn_time = 4.4 # seconds
n_motor = Motor(n_fuel_mass, n_trust_avg, n_total_impulse, n_total_burn_time)



z0 = 0 # m
zv0 = 0 # m/s
za0 = 0 # m/s**2
stateinitial = np.array([z0, zv0, rocket_Ambition.rocket_mass_0])

time = np.arange(0, 63, 0.001)
# Integratoin of model


def simulation(inital_conditions: np.array, time: np.array, rocket: RocketConfig, motor: Motor):
    stateout = sci.odeint(Derivative, inital_conditions, time, args=(rocket, motor,))
    
    zout = stateout[:,0]
    zvout = stateout[:,1]
    massout = stateout[:,2]



    # Results 
    print('\n\n\nResults:')
    print(f'Apogee:  {np.max(zout):.2f}')
    print(f'Maxium Velocity:  {np.max(zvout):.2f}')
    print(f'ISP:  {np.max(n_motor.ISP):.2f}')
    print('\n')

    return stateout

stateout = simulation(stateinitial, time, rocket_Ambition, n_motor)

zout = stateout[:,0]
zvout = stateout[:,1]
massout = stateout[:,2]



# Results 
print('\n\n\nResults:')
print(f'Apogee:  {np.max(zout):.2f}')
print(f'Maxium Velocity:  {np.max(zvout):.2f}')
print(f'ISP:  {np.max(n_motor.ISP):.2f}')
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



