from cProfile import label
from shutil import move
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QIcon, QPixmap


import sys 



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('RoletaVip')
        self.setGeometry(300, 200, 800, 600) #x, y, w, h, -> esq, top, largura, altura
        self.setMinimumHeight(100)
        self.setMinimumWidth(500)
        self.setMaximumHeight(900)
        self.setMaximumWidth(1000)
        self.setToolTip('Roleta Vip')
    



        self.setAutoFillBackground(True)
        self.setStyleSheet('background-color: lightblue;')


        appIcon = QIcon('img/icone.jpg')
        self.setWindowIcon(appIcon)

        self.set_img()


    def set_img(self):
        #primeiro icone
        icone1 = QIcon('img/Roleta_1.jpg')
        label1 = QLabel('Roleta', self)
        pixmap1 = icone1.pixmap(100, 100, QIcon.Active)

        label1.setPixmap(pixmap1)

        #segundo icone 
        icone2 = QIcon('img/Roleta_2.jpg')
        label2 = QLabel('Estrategia', self)
        label2.move = (100, 0)
        pixmap2 = icone2.pixmap(100, 100,  QIcon.Disabled)

        label2.setPixmap(pixmap2)

        #terceiro icone 
        
        icone3 = QIcon('img/Roleta_3.jpg')
        label3 = QLabel('Cuprier', self)
        pixmap3 = icone3.pixmap(100, 100,  QIcon.Selected)
        label3.move = (100, 0)
        label3.setPixmap(pixmap3)





myApp = QApplication(sys.argv)


janela = Window()
janela.show()

myApp.exec_()
sys.exit(0)
