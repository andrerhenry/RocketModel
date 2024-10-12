from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtGui import QFont

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class FigureWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.parent = parent
        self.data = parent.data
        
        dataComboLabel = QtWidgets.QLabel()
        dataComboLabel.setFixedSize(200,16)
        font = QFont()
        font.setBold(True)
        dataComboLabel.setFont(font)
        dataComboLabel.setText("Plot Selected Data:")
                
        self.dataComboBox = QtWidgets.QComboBox()
        self.dataComboBox.addItems(self.data.meta_data.keys())
        self.dataComboBox.currentTextChanged.connect(self.updateCanvas)
        
        header = QtWidgets.QWidget()
        headerLayout = QtWidgets.QHBoxLayout()
        headerLayout.addWidget(dataComboLabel)
        headerLayout.addWidget(self.dataComboBox)
        header.setLayout(headerLayout)
        
        self.figureCanvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.figureCanvas.setMinimumSize(800, 500)
        self.axes = self.figureCanvas.figure.subplots()                
        self.updateCanvas()
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(NavigationToolbar(self.figureCanvas, self))
        layout.addWidget(self.figureCanvas)
        layout.addWidget(header)
    
    @Slot()
    def updateCanvas(self):
        self.axes.cla() # clear axes for fresh plot
        key = self.dataComboBox.currentText()
        
        self.axes.plot(self.data.time, getattr(self.data, self.data.meta_data[key]["data"]))
        self.axes.grid()
        self.axes.set_title(key)
        self.axes.set_ylabel(self.data.meta_data[key]["label"])
        self.axes.set_xlabel("Time (s)")
        self.figureCanvas.draw()
