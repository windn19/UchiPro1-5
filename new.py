import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from design import Ui_MainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()

    sys.exit(app.exec_())
