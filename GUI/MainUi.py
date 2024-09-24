import sys
import os
from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import Slot

# Add the parent directory to the system path for user class import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from RocketConfigUi import RocketConfigUi
from MotorConfigUi import MotorConfigUi
#from Rocket_Config import RocketConfig

class MainUi(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        #self.rocket
        self.

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)


        geometry = self.screen().availableGeometry()
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)




if __name__ == "__main__":
    
    
    # testing .ui
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUi()
    ui.show()
    
    sys.exit(app.exec())
    