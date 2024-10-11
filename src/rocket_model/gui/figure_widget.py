from PySide6 import QtWidgets
from PySide6.QtCore import Slot

from matplotlib.backends.backend_qtagg import FigureCanvasQT
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class FigureWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.parent = parent
        self.data = parent.data
        self.data_dict = create_data_dict()
        
        self.dataComboLabel = QtWidgets.QLabel()
        self.dataComboLabel.setText("Plot Data:")
                
        self.dataComboBox = QtWidgets.QComboBox()
        self.dataComboBox.addItems(self.data_dict.keys())
        self.dataComboBox.currentTextChanged.connect(self.updateCanvas)
        
        header = QtWidgets.QWidget()
        headerLayout = QtWidgets.QHBoxLayout()
        headerLayout.addWidget(self.dataComboLabel)
        headerLayout.addWidget(self.dataComboBox)
        header.setLayout(headerLayout)
        
        self.figureCanvas = FigureCanvasQT(Figure(figsize=(5, 3)))
        self.figureCanvas.setMinimumSize(600, 400)
        self.axes = self.figureCanvas.figure.subplots()                
        self.updateCanvas()
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(header)
        layout.addWidget(NavigationToolbar(self.figureCanvas, self))
        layout.addWidget(self.figureCanvas)
    
    @Slot()
    def updateCanvas(self):
        self.axes.cla() # clear axes for fresh plot
        data_key = self.dataComboBox.currentText()
        
        self.axes.plot(self.data.time, getattr(self.data, self.data_dict[data_key]["data"]))
        self.axes.grid()
        self.axes.set_title(data_key)
        self.axes.set_ylabel(self.data_dict[data_key]["label"])
        self.axes.set_xlabel("Time (s)")
        self.figureCanvas.draw()
    
        
def create_data_dict()-> dict:
    """Generates a dictionary conatianing the associated ploting elements
    for the attribute that is plotted. 
    
    key 1: Labelfor plots
    key 2: Units for data
    key 3: Attributes names for the SimulationData class, to select data with key 
    
    Returns:
        dict: figure elements and keys
    """    
    data_dict = {
    "Altitude": {"label": "Altitude (m)", "units": "(m)", "data": "altitude"},
    "Velocity": {"label": "Velocity (m/s)", "units": "(m/s)", "data": "velocity"},
    #"Acceleration": {"label": "Acceleration (m/s^2)", "units": "(m/s^2)", "data": "acceleration"},
    "Mass": {"label": "Mass (kg)", "units": "(kg)", "data": "mass"}
    }
    
    return data_dict

