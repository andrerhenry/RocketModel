import sys
import os
from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QKeySequence, QPixmap
from PySide6.QtCore import Slot, Qt

# Add the parent directory to the system path for user class import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Rocket_Config import RocketConfig, Motor
from Simulation_Config import simulation, Time
from RocketConfigUi import RocketConfigUi
from MotorConfigUi import MotorConfigUi
from SimulationConfigUi import SimulationUi
#from FlightCalculator import *


class MainUi(QtWidgets.QMainWindow):
    def __init__(self, rocket: RocketConfig, motor: Motor, time: Time, parent = None):
        super().__init__(parent)
        self. rocket = rocket
        self. motor = motor
        self.time = time
        
        centralWidget = QtWidgets.QWidget()
        configWidget = QtWidgets.QWidget()
        configWidget.setFixedWidth(225)
        #configWidget.layoutDirection().LeftToRight
        
        self.logoLabel = QtWidgets.QLabel()
        #logoPath = QPixmap("GUI/HornetLogo.png").scaledToWidth(configWidget.width(), mode = Qt.SmoothTransformation)
        logoPath = QPixmap("GUI/HornetLogo.png").scaled(configWidget.width(), configWidget.width(), aspectMode = Qt.KeepAspectRatio , mode = Qt.SmoothTransformation)
        self.logoLabel.setPixmap(logoPath)
        #self.logoLabel.setPixmap(logoPath.scaled(self.logoLabel.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))        
               

        
        rocketConfigWidget = RocketConfigUi(rocket, self)
        motorConfigWidget = MotorConfigUi(motor, self)
        simulationConfigWidget = SimulationUi(self)
        
        configLayout = QtWidgets.QVBoxLayout()
        configLayout.addWidget(self.logoLabel)
        configLayout.addWidget(rocketConfigWidget)
        configLayout.addWidget(motorConfigWidget)
        configWidget.setLayout(configLayout)
        
        
        
        
        centralLayout = QtWidgets.QHBoxLayout()
        centralLayout.addWidget(configWidget, alignment = Qt.AlignmentFlag.AlignLeft)
        centralLayout.addWidget(simulationConfigWidget, alignment=Qt.AlignmentFlag.AlignTop)
        centralWidget.setLayout(centralLayout)
        self.setCentralWidget(centralWidget)
        
    @Slot()
    def runSimulation(self):
        inital_conditions = [0, 0, rocket.rocket_mass_0]
        simulation(inital_conditions, self.time.time_array(), self.rocket, self.motor)
            
            
        
        self.addAction
        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)


        #geometry = self.screen().availableGeometry()
        #self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)
        





if __name__ == "__main__":
    
    # testing rocket data
    rocket_mass_0 = 32098/1000 # kilograms
    drag_coefficient = 0.36 #cf
    diameter = 0.155 # meters
    rocket = RocketConfig(rocket_mass_0, drag_coefficient, diameter)
    
    # n Rocket Motor Perameters
    FuelMass = 7512.0/1000.0 # kg
    ThrustAvg = 3168.0 # F
    TotalImpulse = 14041.0 # Ns
    burn_time = 4.4 #s
    Nmotor = Motor(FuelMass, ThrustAvg, TotalImpulse, burn_time)
    
    time = Time(0, 63, 0.001)
    
    
    # testing .ui
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUi(rocket, Nmotor, time)
    ui.show()
    
    sys.exit(app.exec())
    