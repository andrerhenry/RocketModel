
import sys
import os

# Add the parent directory to the system path to import classes
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6 import QtCore, QtGui, QtWidgets
from Rocket_Config import RocketConfig

def x(input): print(input) # Temp var 


class RocketConfigUi(QtWidgets.QWidget):
    def __init__(self, rocket: RocketConfig, parent = None):
        super(RocketConfigUi, self).__init__(parent)
       
        self.configLabel = QtWidgets.QLabel()
        self.configLabel.setGeometry(QtCore.QRect(0, 15, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.configLabel.setFont(font)
        self.configLabel.setText("Rocket Configuration:")
        
        self.rocketMassLabel = QtWidgets.QLabel()
        self.rocketMassLabel.setGeometry(QtCore.QRect(0, 50, 100, 16))
        self.rocketMassLabel.setText("Rocket Mass (kg):")
        
        self.rocketMassEdit = QtWidgets.QLineEdit()
        self.rocketMassEdit.setGeometry(QtCore.QRect(150, 50, 100, 20))
        self.rocketMassEdit.setText(str(rocket.rocket_mass_0))
        self.rocketMassEdit.editingFinished.connect(lambda: x(self.rocketMassEdit.text()))
                
        self.dragCoefLabel = QtWidgets.QLabel()
        self.dragCoefLabel.setGeometry(QtCore.QRect(0, 75, 100, 16))
        self.dragCoefLabel.setText("C_d: ")
        
        self.dragCoefEdit = QtWidgets.QLineEdit()
        self.dragCoefEdit.setGeometry(QtCore.QRect(150, 75, 100, 20))
        self.dragCoefEdit.setText("editCoeDrag")
        self.dragCoefEdit.editingFinished.connect(lambda: x(self.dragCoefEdit.text()))
                
        self.diameterLabel = QtWidgets.QLabel()
        self.diameterLabel.setGeometry(QtCore.QRect(0, 100, 100, 16))
        self.diameterLabel.setText("Diameter (m):")
        
        self.diameterEdit = QtWidgets.QLineEdit()
        self.diameterEdit.setGeometry(QtCore.QRect(150, 100, 100, 20))
        self.diameterEdit.setText("editDiameter")
        self.diameterEdit.editingFinished.connect(lambda: x(self.diameterEdit.text()))

        formLayout = QtWidgets.QFormLayout(self)
        formLayout.addRow(self.configLabel)
        formLayout.addRow(self.rocketMassLabel, self.rocketMassEdit)
        formLayout.addRow(self.dragCoefLabel, self.dragCoefEdit)
        formLayout.addRow(self.diameterLabel, self.diameterEdit)
        
    def func():
        pass


if __name__ == "__main__":
    # testing rocket data
    rocket_mass_0 = 32098/1000 # kilograms
    drag_coefficient = 0.36 #cf
    diameter = 0.155 # meters
    rocket = RocketConfig(rocket_mass_0, drag_coefficient, diameter)
    
    # testing .ui
    app = QtWidgets.QApplication()
    ui = RocketConfigUi(rocket)
    ui.show()
    
    sys.exit(app.exec())
    