import sys
import time

import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Slot


from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class FigureWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.parent = parent
        self.figure_elements = figure_dict()
        
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setText("update graph")
        self.pushButton.clicked.connect(self.update_canvas)
        
        self.dataComboBox = QtWidgets.QComboBox()
        self.dataComboBox.addItems(self.figure_elements.keys())
        #self.dataComboBox.addItems(["Altitude", "Velocity", "Mass"])
        self.dataComboBox.currentTextChanged.connect(self.comboBoxChanged)
        
        
        self.figureCanvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.figureCanvas.setMinimumSize(600, 400)
        self.axes = self.figureCanvas.figure.subplots()                
        self.update_canvas()
        
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.dataComboBox)
        layout.addWidget(NavigationToolbar(self.figureCanvas, self))
        layout.addWidget(self.figureCanvas)
    
    @Slot()
    def update_canvas(self):
        self.axes.cla()
        print("the button is pressed")
        self.axes.plot(self.parent.data.time, self.parent.data.altitude)
        self.axes.grid()
        self.axes.set_title("Altitude")
        self.axes.set_ylabel("Altitude (m)")
        self.axes.set_xlabel("Time (s)")
        self.figureCanvas.draw()
    
    @Slot()
    def comboBoxChanged(self):
        print(self.dataComboBox.currentText())

        
        
def figure_dict()-> dict:
    """Generates a dictionary conatianing the associated ploting elements
    for the attribute that is plotted. 
    
    The dict can be modified to contain other information to be passed 
    describing the atribute.

    Returns:
        dict: figure elements 
    """    
    figure_elements = {
    "Alititude" : {"label": "Altitude (m)", "units": "(m)"},
    "Velocity" : {"label": "Velocity (m/s)", "units": "(m/s)"},
    "Acceleration" : {"label": "Acceleration (m/s^2)", "units": "(m/s^2)"},
    "Mass" : {"label": "Mass (kg)", "units": "(kg)"}
    }
    
    return figure_elements

