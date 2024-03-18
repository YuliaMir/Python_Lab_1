'''Разработайте счетчик нажатий на кнопку, который меняет
свою надпись на число нажатий на нее (1, 2, 3 и т.д.)'''

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class ClickCounter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton('Click me', self)
        self.button.clicked.connect(self.buttonClicked)
        self.counter = 0

        self.setGeometry(100, 100, 200, 100)
        self.setWindowTitle('Click Counter')
        self.show()

    def buttonClicked(self):
        self.counter += 1
        self.button.setText(f'Clicked {self.counter} times')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClickCounter()
    sys.exit(app.exec())
