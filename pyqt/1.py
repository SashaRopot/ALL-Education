from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []
        self.operand_1 = []
        self.operand_2 = []

    def initUI(self):
        self.setGeometry(300, 300, 225, 370)
        self.setWindowTitle("Калькулятор")

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.resize(225, 95)
        self.move(0, 0)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(5, 100)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(60, 100)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(115, 100)

        self.div = QPushButton('/', self)
        self.div.resize(50, 50)
        self.div.move(170, 100)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(5, 155)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(60, 155)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(115, 155)

        self.mul = QPushButton('*', self)
        self.mul.resize(50, 50)
        self.mul.move(170, 155)

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(50, 50)
        self.num_1.move(5, 210)

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(60, 210)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(115, 210)

        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(170, 210)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(5, 265)

        self.percent = QPushButton('%', self)
        self.percent.resize(50, 50)
        self.percent.move(60, 265)

        self.sqrt = QPushButton('√', self)
        self.sqrt.resize(50, 50)
        self.sqrt.move(115, 265)

        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(170, 265)

        self.c = QPushButton('C', self)
        self.c.resize(50, 50)
        self.c.move(5, 320)

        self.step = QPushButton('^', self)
        self.step.resize(50, 50)
        self.step.move(60, 320)

        self.square = QPushButton('x²', self)
        self.square.resize(50, 50)
        self.square.move(115, 320)

        self.ravno = QPushButton('=', self)
        self.ravno.resize(50, 50)
        self.ravno.move(170, 320)

        self.ost = QPushButton('//', self)
        self.ost.resize(50, 50)
        self.ost.move(170, 45)

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.div.clicked.connect(self.div_1)
        self.mul.clicked.connect(self.mul_1)
        self.sqrt.clicked.connect(self.sqrt_1)
        self.step.clicked.connect(self.step_1)
        self.ravno.clicked.connect(self.ravno_1)
        self.c.clicked.connect(self.clear)
        self.square.clicked.connect(self.square_1)
        self.percent.clicked.connect(self.percent_1)
        self.ost.clicked.connect(self.ost_1)

    def enterValue(self):
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def step_1(self):
        self.operation = '^'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def sqrt_1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def square_1(self):
        self.operation = 'x²'
        self.operand_1 = float(self.label.text())
        self.rezult = self.operand_1 ** 2
        self.label.setText(str(self.rezult))

    def percent_1(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
        # self.rezult = self.operand_1/100
        # self.label.setText(str(self.rezult))

    def ost_1(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def ravno_1(self):
        self.operand_2 = float(self.label.text())
        if self.operation == '+':
            self.rezult = self.operand_1 + self.operand_2
        if self.operation == '-':
            self.rezult = self.operand_1 - self.operand_2
        if self.operation == '*':
            self.rezult = self.operand_1 * self.operand_2
        if self.operation == '^':
            self.rezult = self.operand_1 ** self.operand_2
        if self.operation == '/':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 / self.operand_2
        if self.operation == '√':
            self.rezult = self.operand_1 ** (1 / self.operand_2)
        self.label.setText(str(self.rezult))
        if self.operation == '//':
            self.rezult = self.operand_1 // self.operand_2
        if self.operation =='%':
            self.rezult = (self.operand_1 * self.operand_2) / 100

    def clear(self):
        self.label.setText('0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
