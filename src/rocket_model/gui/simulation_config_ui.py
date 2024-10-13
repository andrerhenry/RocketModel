from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Slot

from rocket_model.simulation.simulation_config import Time


class SimulationUI(QtWidgets.QWidget):
    def __init__(self, time: Time, parent = None):
        super().__init__(parent)
        self.time = time
        self._parent = parent
       
        self.configLabel = QtWidgets.QLabel()
        self.configLabel.setGeometry(QtCore.QRect(0, 15, 175, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.configLabel.setFont(font)
        self.configLabel.setText("Simulation Configuration:")
        
        self.runButton = QtWidgets.QPushButton("Run Simulation")
        self.runButton.setFixedSize(100,25)
        self.runButton.clicked.connect(self.runButtonClicked)      
        
        self.startTimeLabel = QtWidgets.QLabel()
        self.startTimeLabel.setFixedWidth(75)
        self.startTimeLabel.setText("Start time:") 
        
        self.startTimeEdit = QtWidgets.QLineEdit()
        self.startTimeEdit.setFixedWidth(50)
        self.startTimeEdit.setText(str(time.start_time))
        self.startTimeEdit.editingFinished.connect(self.setStartTime)
        
        self.endTimeLabel = QtWidgets.QLabel()
        self.endTimeLabel.setFixedWidth(75)
        self.endTimeLabel.setText("Max Run Time:") 
        
        self.endTimeEdit = QtWidgets.QLineEdit()
        self.endTimeEdit.setFixedWidth(50)
        self.endTimeEdit.setText(str(time.end_time))
        self.endTimeEdit.editingFinished.connect(self.setEndTime)
        
        self.stepTimeLabel = QtWidgets.QLabel()
        self.stepTimeLabel.setFixedWidth(75)
        self.stepTimeLabel.setText("Step:") 
        
        self.stepTimeEdit = QtWidgets.QLineEdit()
        self.stepTimeEdit.setFixedWidth(50)
        self.stepTimeEdit.setText(str(time.step))
        self.stepTimeEdit.editingFinished.connect(self.setStep)
        
        
        inputBox = QtWidgets.QHBoxLayout(self)
        inputBox.addWidget(self.startTimeLabel)
        inputBox.addWidget(self.startTimeEdit)
        inputBox.addWidget(self.endTimeLabel)
        inputBox.addWidget(self.endTimeEdit)
        inputBox.addWidget(self.stepTimeLabel)
        inputBox.addWidget(self.stepTimeEdit)
        inputBox.addWidget(self.runButton)
        inputWidget = QtWidgets.QWidget()
        inputWidget.setLayout(inputBox)
        
        simulationLayout = QtWidgets.QVBoxLayout(self)
        simulationLayout.addWidget(self.configLabel)
        simulationLayout.addWidget(inputWidget)
        
        
    @Slot()
    def setStartTime(self):
        self.time.start_time = float(self.startTimeEdit.text())

    @Slot()
    def setEndTime(self):
        self.time.end_time = float(self.endTimeEdit.text())
    
    @Slot()
    def setStep(self):
        self.time.step = float(self.stepTimeEdit.text())
        
    @Slot()
    def runButtonClicked(self):
        self._parent.runSimulation()
