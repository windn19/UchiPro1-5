import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.line = QLineEdit(self)
        self.line.move(10, 10)
        self.lbl = QLabel('', self)
        self.lbl.move(10, 100)
        self.button = QPushButton('Push me', self)
        self.button.move(10, 50)
        self.button.clicked.connect(self.on_click)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web1.png'))
        self.show()

    def on_click(self):
        self.lbl.setText(self.line.text())
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())