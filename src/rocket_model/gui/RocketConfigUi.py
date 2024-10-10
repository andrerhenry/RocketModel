import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Slot

from config.Rocket_Config import RocketConfig



class RocketConfigUi(QtWidgets.QWidget):
    def __init__(self, rocket: RocketConfig, parent = None):
        super().__init__(parent)
        self.rocket = rocket
       
        self.configLabel = QtWidgets.QLabel()
        self.configLabel.setGeometry(QtCore.QRect(0, 15, 175, 21))
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
        self.rocketMassEdit.editingFinished.connect(self.setRocketMass)
                
        self.dragCoefLabel = QtWidgets.QLabel()
        self.dragCoefLabel.setGeometry(QtCore.QRect(0, 75, 100, 16))
        self.dragCoefLabel.setText("C_d: ")
        
        self.dragCoefEdit = QtWidgets.QLineEdit()
        self.dragCoefEdit.setGeometry(QtCore.QRect(150, 75, 100, 20))
        self.dragCoefEdit.setText(str(rocket.drag_coefficient))
        self.dragCoefEdit.editingFinished.connect(self.setRocketDragCoef)
                
        self.diameterLabel = QtWidgets.QLabel()
        self.diameterLabel.setGeometry(QtCore.QRect(0, 100, 100, 16))
        self.diameterLabel.setText("Diameter (m):")
        
        self.diameterEdit = QtWidgets.QLineEdit()
        self.diameterEdit.setGeometry(QtCore.QRect(150, 100, 100, 20))
        self.diameterEdit.setText(str(rocket.diameter))
        self.diameterEdit.editingFinished.connect(self.setRocketDiameter)

        formLayout = QtWidgets.QFormLayout(self)
        formLayout.addRow(self.configLabel)
        formLayout.addRow(self.rocketMassLabel, self.rocketMassEdit)
        formLayout.addRow(self.dragCoefLabel, self.dragCoefEdit)
        formLayout.addRow(self.diameterLabel, self.diameterEdit)
        self.setFixedWidth(200)
        
    @Slot()
    def setRocketMass(self):
        self.rocket.rocket_mass_0 = float(self.rocketMassEdit.text())
    
    @Slot()
    def setRocketDragCoef(self):
        self.rocket.drag_coefficient = float(self.dragCoefEdit.text())
    
    @Slot()
    def setRocketDiameter(self):
        self.rocket.diameter = float(self.diameterEdit.text())
   
    