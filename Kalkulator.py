import sys
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QVBoxLayout,QPushButton,QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator")
        vbox= QVBoxLayout()
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        vbox.addWidget(self.result_display)
        self.setLayout(vbox)

        grid = QGridLayout()

        buttons = [("7", self.add_number), ("8", self.add_number), ("9", self.add_number), ("/", self.add_operator),
                   ("4", self.add_number), ("5", self.add_number), ("6", self.add_number), ("*", self.add_operator),
                   ("1", self.add_number), ("2", self.add_number), ("3", self.add_number), ("-", self.add_operator),
                   ("0", self.add_number), ("C", self.add_clear), (".", self.add_decimal), ("+", self.add_operator),
                   ("Bksp", self.add_backspace), ("=", self.add_calculate) ]
        col, row = 0,0
        for text, func in buttons:
            button = QPushButton(text)
            button.clicked.connect(func)
            grid.addWidget(button, row, col)
            col+=1
            if col==4:
                row+=1
                col=0

        vbox.addLayout(grid)

    def add_number(self):
        sender = self.sender()
        self.result_display.setText(self.result_display.text()+sender.text())
    def add_backspace(self):
        self.result_display.setText(self.result_display.text()[:-1])
    def add_clear(self):
        self.result_display.clear()
    def add_operator(self):
        pass
    def add_decimal(self):
        pass
    def add_calculate(self):
        pass



app= QApplication(sys.argv)
calculator = CalculatorApp()
calculator.show()
sys.exit(app.exec_())