from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow
import sys


def window():
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    win = QMainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
