import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText('Hello World')
    w.setGeometry(100, 100, 200, 200)
    b.move(50, 20)
    w.setWindowTitle('PyQt')
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
