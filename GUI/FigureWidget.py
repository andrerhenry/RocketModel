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
        
        self.figureCanvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.figureCanvas.setMinimumSize(600, 400)
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setText("update graph")
        self.pushButton.clicked.connect(self.update_canvas)
        
        self.axes = self.figureCanvas.figure.subplots()
                
        self.update_canvas()
        # Set up a Line2D.
        #self._line, = self.axes.plot(t, np.sin(t + time.time()))
        #self.axes.plot(self.parent.data.t, self.parent.data.x)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.pushButton)
        layout.addWidget(NavigationToolbar(self.figureCanvas, self))
        layout.addWidget(self.figureCanvas)
    
    @Slot()
    def update_canvas(self):
        self.axes.cla()
        print("the button is pressed")
        self.axes.plot(self.parent.data.time, self.parent.data.altitude)
        self.axes.grid()
        self.axes.set_title("Altitude")
        self.axes.set_xlabel("Time (s)")
        self.axes.set_ylabel("Altitude (m)")
        self.figureCanvas.draw()


if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = FigureWidget()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec()