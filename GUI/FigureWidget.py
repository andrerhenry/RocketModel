import sys
import time

import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Slot


from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure


class FigureWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.parent = parent

        self.figureCanvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.clicked.connect(self._update_canvas)
        
        self.axes = self.figureCanvas.figure.subplots()
        
        # Set up a Line2D.
        #self._line, = self.axes.plot(t, np.sin(t + time.time()))
        self.axes.plot(self.parent.data.t, self.parent.data.x)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.pushButton)
        layout.addWidget(NavigationToolbar(self.figureCanvas, self))
        layout.addWidget(self.figureCanvas)
    
    @Slot()
    def _update_canvas(self):
        self.axes.cla()
        print("the button is pressed")
        self.axes.plot(self.parent.data.time, self.parent.data.altitude)
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