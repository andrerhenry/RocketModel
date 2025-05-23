""" Rocket Flight Model
    Author: Andre Henry
    Date: 10/9/2024

    This Code is to provide rough flight calcuation data for a Rocket desing. 
    Assumtions in this code:
        *Gravity is constaint
        *Rocket AOA is zero
        *Rocket is stable and rigid
        *Motor is considered to burn evenly consitantly for the burn time
"""

import sys
import time
from pathlib import Path
from PySide6 import QtWidgets, QtGui

from rocket_model.config import RocketConfig, Motor
from rocket_model.simulation.simulation import Time
from rocket_model.gui.main_ui import MainUi



# Defulat perameters to use in GUI
# Rocket: Ambition
rocket_mass_0 = 32098 / 1000 # kilograms
drag_coefficient = 0.36 #cf
diameter = 0.155 # meters
rocket_Ambition = RocketConfig(rocket_mass_0, drag_coefficient, diameter)

# N Motor Perameters
n_fuel_mass = 7512 / 1000 # kg
n_trust_avg = 3168.0 # Newtons
n_total_impulse = 14041.0 # Newton*seconds
n_total_burn_time = 4.4 # seconds
n_motor = Motor(n_fuel_mass, n_trust_avg, n_total_impulse, n_total_burn_time)

time_config = Time(0, 80, 0.001)


app = QtWidgets.QApplication(sys.argv)

base_dir = Path(__file__).parent
splash_path = base_dir/"gui"/"images"/"splash.png"
splash = QtWidgets.QSplashScreen(QtGui.QPixmap(splash_path).scaled(700, 700))
splash.show()
time.sleep(1)
app.processEvents()

ui = MainUi(rocket_Ambition, n_motor, time_config)
ui.show()
splash.finish(ui)
sys.exit(app.exec())






