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

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QKeySequence, QPixmap
from PySide6.QtCore import Slot, Qt

from Rocket_Config import RocketConfig, Motor
from Aero_Config import Aero
from Simulation_Config import simulation, Time

#from GUI.MainUi import MainUi

plt.ion # Interactive mode in plots





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

time = Time(0, 63, 0.001)
# Integratoin of model

stateout = simulation(stateinitial, time.time_array(), rocket_Ambition, n_motor)

zout = stateout[:,0]
zvout = stateout[:,1]
massout = stateout[:,2]


"""
# testing .ui
app = QtWidgets.QApplication(sys.argv)
ui = MainUi(rocket_Ambition, n_motor, time)
ui.show()

sys.exit(app.exec())
"""

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



