import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.y = 1

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web1.png'))

        button = QPushButton('Button', self)
        button.move(100, 10)
        button.clicked.connect(self.on_click)

        b_add = QPushButton('Add', self)
        b_add.move(10, 10)
        b_add.clicked.connect(self.on_add)
        self.layout = QVBoxLayout(self)
        self.layout.setGeometry(QRect(20, 10, 300, 200))
        self.show()

    def on_click(self):
        print('Button click')

    def on_add(self):
        self.list = QLineEdit(self)
        self.label = QLabel('Test', self)


        self.layout.addStretch(1)
        self.layout.addWidget(self.list)
        self.layout.addWidget(self.label)
        # self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())
