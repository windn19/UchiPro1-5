import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web1.png'))
        self.label = QLabel('Текст для вывода', self)
        self.label.move(100, 100)
        self.label.adjustSize()
        self.button = QPushButton('Нажми меня!', self)
        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        # QMessageBox.question(self, 'Message', 'Are you sure to quit?',
        #                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # QMessageBox.information(self, 'Message', 'Hello, world!!!', QMessageBox.Ok)
        self.label.setText('Новый текст!!!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())