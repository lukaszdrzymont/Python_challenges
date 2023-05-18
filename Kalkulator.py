import sys
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QGridLayout,QLineEdit,QApplication

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator")
        vbox = QVBoxLayout()
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        vbox.addWidget(self.result_display)

        self.setLayout(vbox)

        buttons = [("7", self.add_number), ("8", self.add_number), ("9", self.add_number), ("/", self.add_operator),
                   ("4", self.add_number), ("5", self.add_number), ("6", self.add_number), ("*", self.add_operator),
                   ("1", self.add_number), ("2", self.add_number), ("3", self.add_number), ("-", self.add_operator),
                   ("0", self.add_number), ("C", self.add_clear), (".", self.add_decimal), ("+", self.add_operator),
                   ("Bksp", self.add_backspace), ("=", self.add_calculate), ]
        col, row = 0,0
        grid = QGridLayout()
        for text, func in buttons:
            button = QPushButton(text)
            button.clicked.connect(func)
            grid.addWidget(button,row,col)
            col+=1
            if col==4:
                row+=1
                col=0
        vbox.addLayout(grid)

        self.new_number = True
        self.memory = None
        self.current_operator = None


    def add_number(self):
        if self.new_number:
            self.result_display.clear()
            self.new_number = False
        sender = self.sender()
        self.result_display.setText(self.result_display.text()+sender.text())
    def add_decimal(self):
        if "." not in self.result_display.text():
            self.result_display.setText(self.result_display.text()+".")
    def add_clear(self):
        self.result_display.clear()
        self.new_number = True
        self.memory = None
        self.current_operator = None

    def add_backspace(self):
        self.result_display.setText(self.result_display.text()[:-1])
    def add_operator(self):
        if not self.new_number:
            if self.memory is None:
                self.memory = float(self.result_display.text())
            else:
                self.add_calculate()
            self.current_operator = self.sender().text()
            self.new_number = True

    def add_calculate(self):
        if self.memory is not None and self.current_operator is not None and not self.new_number:
            right_operand = float(self.result_display.text())
            if self.current_operator == "+":
                result = self.memory + right_operand
            elif self.current_operator == "-":
                result = self.memory - right_operand
            elif self.current_operator == "*":
                result = self.memory * right_operand
            else:
                if right_operand !=0:
                    result = self.memory / right_operand
                else:
                    result = "Błąd, dzielenie przez zero"
            self.result_display.setText(str(result))
            self.new_number= True
            self.memory = None
            self.current_operator = None

app = QApplication(sys.argv)
calculator = CalculatorApp()
calculator.show()
sys.exit(app.exec_())