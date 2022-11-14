import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

import qres

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.setWindowIcon(QIcon(':web'))
    # print(QIcon(':web').Active)
    w.show()
    sys.exit(app.exec_())
