
import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Slot

# Add the parent directory to the system path for user class import
if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from Simulation_Config import Time



class SimulationUi(QtWidgets.QWidget):
    def __init__(self, time:Time, parent = None):
        super().__init__(parent)
        self.time = time
        self.parent = parent
        
       
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
        self.startTimeLabel.setFixedWidth(25)
        self.startTimeLabel.setText("Start:") 
        
        self.startTimeEdit = QtWidgets.QLineEdit()
        self.startTimeEdit.setFixedWidth(50)
        self.startTimeEdit.setText(str(time.start_time))
        self.startTimeEdit.editingFinished.connect(self.setStartTime)
        
        self.endTimeLabel = QtWidgets.QLabel()
        self.endTimeLabel.setFixedWidth(25)
        self.endTimeLabel.setText("End:") 
        
        self.endTimeEdit = QtWidgets.QLineEdit()
        self.endTimeEdit.setFixedWidth(50)
        self.endTimeEdit.setText(str(time.end_time))
        self.endTimeEdit.editingFinished.connect(self.setEndTime)
        
        self.stepTimeLabel = QtWidgets.QLabel()
        self.stepTimeLabel.setFixedWidth(25)
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
        print("set start time")
        self.time.start_time = float(self.startTimeEdit.text())

    @Slot()
    def setEndTime(self):
        print("set end time")
        self.time.end_time = float(self.endTimeEdit.text())
    
    @Slot()
    def setStep(self):
        print("set step ")
        self.time.step = float(self.stepTimeEdit.text())
        
    @Slot()
    def runButtonClicked(self):
        print("run simulation")
        self.parent.runSimulation()
        



if __name__ == "__main__":
    
    time = Time(0, 63, 0.001)
    
    # testing .ui
    app = QtWidgets.QApplication()
    ui = SimulationUi(time)
    ui.show()
    
    sys.exit(app.exec())
    