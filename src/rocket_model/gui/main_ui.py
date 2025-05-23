import numpy as np

from pathlib import Path
from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QKeySequence, QPixmap, QFont
from PySide6.QtCore import Slot, Qt

from rocket_model.config.rocket_config import RocketConfig, Motor
from rocket_model.simulation.simulation import simulation, Time, SimulationData

from rocket_model.gui.rocket_config_ui import RocketConfigUI
from rocket_model.gui.motor_config_ui import MotorConfigUI
from rocket_model.gui.simulation_config_ui import SimulationUI
from rocket_model.gui.figure_widget import FigureWidget


class MainUi(QtWidgets.QMainWindow):
    def __init__(self, rocket: RocketConfig, motor: Motor, time: Time, parent = None):
        super().__init__(parent)
        self.rocket = rocket
        self.motor = motor
        self.time = time
        self.data = SimulationData()
        self.setWindowTitle("Hornet Aerospace and Propultion - Rocket Model")
        
        centralWidget = QtWidgets.QWidget()
        headerWidget = QtWidgets.QWidget()
        interfaceWidget = QtWidgets.QWidget()
        configWidget = QtWidgets.QWidget()
        configWidget.setFixedWidth(225)
        simulationWidget = QtWidgets.QWidget()
        
        base_dir = Path(__file__).parent
        imagePath = base_dir/"images"/"HornetLogo.png"
        logoPath = QPixmap(imagePath).scaled(
            configWidget.width(),
            configWidget.width(),
            aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
            mode=Qt.TransformationMode.SmoothTransformation
        )
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

        
        rocketConfigWidget = RocketConfigUI(self.rocket, self)
        motorConfigWidget = MotorConfigUI(self.motor, self)
        self.textbox = QtWidgets.QTextEdit()
        
        configLayout = QtWidgets.QVBoxLayout()
        configLayout.addWidget(rocketConfigWidget)
        configLayout.addWidget(motorConfigWidget)
        configLayout.addWidget(self.textbox)
        configWidget.setLayout(configLayout)
        
        
        simulationConfigWidget = SimulationUI(self.time, self)
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
        exit_action.triggered.connect(self.close)
        
        
    @Slot()
    def runSimulation(self):
        inital_conditions = np.array([0, 0, self.rocket.rocket_mass_0])
        time_array, state, state_dot = simulation(inital_conditions, self.time, self.rocket, self.motor)
        self.data.update_data(time_array, state, state_dot, self)
        self.figureWidget.updateCanvas()
        
    @Slot()
    def appendText(self, text):
        self.textbox.append(text)


