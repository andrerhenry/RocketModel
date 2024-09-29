
import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Slot

# Add the parent directory to the system path for user class import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from FlightCalculator import *


class SimulationUi(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        
        
        self.runButton = QtWidgets.QPushButton("Run Simulation")
        self.runButton.setFixedSize(100,25)
        self.runButton.clicked.connect(self.runSimulation)
       
        self.configLabel = QtWidgets.QLabel()
        self.configLabel.setGeometry(QtCore.QRect(0, 15, 175, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.configLabel.setFont(font)
        self.configLabel.setText("Simulation Configuration:")
        
              
        

        formLayout = QtWidgets.QFormLayout(self)
        formLayout.addRow(self.configLabel)
        formLayout.addRow(self.runButton)
        
        
    @Slot()
    def runSimulation(self):
        print("run simulation")
        simulation(stateinitial, time, rocket_Ambition, n_motor)
    

        
    


if __name__ == "__main__":
    # testing rocket data
    
    # testing .ui
    app = QtWidgets.QApplication()
    ui = SimulationUi()
    ui.show()
    
    sys.exit(app.exec())
    