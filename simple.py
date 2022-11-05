import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.setWindowIcon(QIcon('web1.png'))
    w.show()
    sys.exit(app.exec_())
