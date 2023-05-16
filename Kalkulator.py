import sys
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QHBoxLayout,QVBoxLayout,QPushButton,QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator")



app = QApplication(sys.argv)
calculator = CalculatorApp()
calculator.show()
sys.exit(app.exec_())