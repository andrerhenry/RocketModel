""" Rocket Flight Calculator
    Author: Andre Henry
    Date: 5/12/2024

    This Code is to providoe rough flight calcuation data for a Rocket desing. 
    Assumtions in this code:
        *Gravity is constaint
        *Rocket AOA is zero
        *Rocket is stable and rigid
        *Motor is considered to burn even andn consitantly for the burn time
"""
__version__ = "2.0.0"

import sys
from PySide6 import QtWidgets

from Config import RocketConfig, Motor
from Config.Simulation_Config import Time
from GUI.MainUi import MainUi


# Defulat perameters to use in GUI
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

time = Time(0, 63, 0.001)


app = QtWidgets.QApplication(sys.argv)
ui = MainUi(rocket_Ambition, n_motor, time)
ui.show()

sys.exit(app.exec())






