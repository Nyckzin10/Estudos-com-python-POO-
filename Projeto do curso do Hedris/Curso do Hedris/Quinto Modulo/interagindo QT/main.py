import sys
from designer01 import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    qt.exec_()