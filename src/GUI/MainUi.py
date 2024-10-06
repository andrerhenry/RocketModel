import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QKeySequence, QPixmap, QFont
from PySide6.QtCore import Slot, Qt

from Config.Rocket_Config import RocketConfig, Motor
from Config.Simulation_Config import simulation, Time, SimulationData

from GUI.RocketConfigUi import RocketConfigUi
from GUI.MotorConfigUi import MotorConfigUi
from GUI.SimulationConfigUi import SimulationUi
from GUI.FigureWidget import FigureWidget



class MainUi(QtWidgets.QMainWindow):
    def __init__(self, rocket: RocketConfig, motor: Motor, time: Time, parent = None):
        super().__init__(parent)
        self.rocket = rocket
        self.motor = motor
        self.time = time
        self.data = SimulationData()
        
        centralWidget = QtWidgets.QWidget()
        headerWidget = QtWidgets.QWidget()
        interfaceWidget = QtWidgets.QWidget()
        configWidget = QtWidgets.QWidget()
        configWidget.setFixedWidth(225)
        simulationWidget = QtWidgets.QWidget()
        
        logoPath = QPixmap("src\\GUI\\Images\\HornetLogo.png").scaled(configWidget.width(), configWidget.width(), aspectMode = Qt.KeepAspectRatio , mode = Qt.SmoothTransformation)
        logoLabel = QtWidgets.QLabel()
        logoLabel.setPixmap(logoPath)
        
        titleLabel = QtWidgets.QLabel()
        titleLabel.setText("Rocket Model")
        titleFont = QFont()
        titleFont.bold()
        titleFont.setPointSize(20)
        titleLabel.setFont(titleFont)
        
        headerLayout = QtWidgets.QHBoxLayout()
        headerLayout.addWidget(logoLabel)
        headerLayout.addWidget(titleLabel, alignment = Qt.AlignmentFlag.AlignLeading.AlignLeft)
        headerLayout.addStretch()
        headerWidget.setLayout(headerLayout)

        
        rocketConfigWidget = RocketConfigUi(self.rocket, self)
        motorConfigWidget = MotorConfigUi(self.motor, self)
        
        configLayout = QtWidgets.QVBoxLayout()
        configLayout.addWidget(rocketConfigWidget)
        configLayout.addWidget(motorConfigWidget)
        #configLayout.addStretch()
        configWidget.setLayout(configLayout)
        
        
        simulationConfigWidget = SimulationUi(self.time, self)
        self.figureWidget = FigureWidget(self)
        
        simulationLayout = QtWidgets.QVBoxLayout()
        simulationLayout.addWidget(simulationConfigWidget)
        simulationLayout.addWidget(self.figureWidget)
        simulationLayout.addStretch()
        simulationWidget.setLayout(simulationLayout)
        
        interfaceLayout = QtWidgets.QHBoxLayout()
        interfaceLayout.addWidget(configWidget, alignment = Qt.AlignmentFlag.AlignLeft)
        interfaceLayout.addWidget(simulationWidget, alignment=Qt.AlignmentFlag.AlignTop)
        interfaceWidget.setLayout(interfaceLayout)
               
        
        centralLayout = QtWidgets.QVBoxLayout()
        centralLayout.addWidget(headerWidget)
        centralLayout.addWidget(interfaceWidget)
        centralWidget.setLayout(centralLayout)
        self.setCentralWidget(centralWidget)
        
        self.addAction
        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        
        
    @Slot()
    def runSimulation(self):
        inital_conditions = [0, 0, self.rocket.rocket_mass_0]
        statevector = simulation(inital_conditions, self.time.time_array(), self.rocket, self.motor)
        self.data.update_data(statevector, self.time.time_array())
        self.figureWidget.updateCanvas()


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
    