
import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets

# Add the parent directory to the system path for user class import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Rocket_Config import Motor


class MotorConfigUi(QtWidgets.QWidget):
    def __init__(self, motor: Motor, parent = None):
        super(MotorConfigUi, self).__init__(parent)
        self.motor = motor
       
        self.configLabel = QtWidgets.QLabel()
        self.configLabel.setGeometry(QtCore.QRect(0, 15, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.configLabel.setFont(font)
        self.configLabel.setText("Motor Configuration:")
        
        self.fuelMassLabel = QtWidgets.QLabel()
        self.fuelMassLabel.setGeometry(QtCore.QRect(0, 50, 100, 16))
        self.fuelMassLabel.setText("Fuel Mass (kg):")
        
        self.fuelMassEdit = QtWidgets.QLineEdit()
        self.fuelMassEdit.setGeometry(QtCore.QRect(150, 50, 100, 20))
        self.fuelMassEdit.setText(str(self.motor.mass_fuel))
        self.fuelMassEdit.editingFinished.connect(self.setFuelMass)
                
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
        formLayout.addRow(self.fuelMassLabel, self.fuelMassEdit)
        formLayout.addRow(self.dragCoefLabel, self.dragCoefEdit)
        formLayout.addRow(self.diameterLabel, self.diameterEdit)
        
    def setFuelMass(self):
        self.motor.rocket_mass_0 = float(self.fuelMassEdit.text())
        print(self.motor.rocket_mass_0)
        print(type(self.motor.rocket_mass_0))
        
    def setRocketDragCoef(self):
        self.motor.drag_coefficient = float(self.dragCoefEdit.text())
        print(self.motor.drag_coefficient)
        print(type(self.motor.drag_coefficient))
    
    def setRocketDiameter(self):
        print("\n\n")
        print(self.motor.diameter)
        print(self.motor._cross_sect_area)
        self.motor.diameter = float(self.diameterEdit.text())
        print(self.motor.diameter)
        print(type(self.motor.diameter))
        print(self.motor._cross_sect_area)
        
    


if __name__ == "__main__":
    
    # n Rocket Motor Perameters
    FuelMass = 7512.0/1000.0 # kg
    ThrustAvg = 3168.0 # F
    TotalImpulse = 14041.0 # Ns
    burn_time = 4.4 #s
    Nmotor = Motor(FuelMass, ThrustAvg, TotalImpulse, burn_time)
   
   
    #print(Nmotor.motor_output(1), type(Nmotor.motor_output(1)) )
    
    # testing .ui
    app = QtWidgets.QApplication()
    ui = RocketConfigUi(Nmotor)
    ui.show()
    
    sys.exit(app.exec())
    