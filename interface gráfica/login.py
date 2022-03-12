from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

import sys 



class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.montar_formulario()

    def montar_formulario(self):
        btn1 = QPushButton('OLá', self)
        btn1.move(20, 100)
        btn1.clicked.connect(self.acao_do_botao)



    def acao_do_botao(self):
        info = QMessageBox.question(self, 'confirmação', 'Seja Bem vindo ao jogo!!',
        QMessageBox.Yes , QMessageBox.No )

        if info == QMessageBox.Yes:
            print(f'Parabéns, o jogo vai começa!')
        else:
            print(f'Eu sabia, você não está preparado para isso..')




myApp = QApplication(sys.argv)

janela = Window()
janela.show()


myApp.exec_()
sys.exit(0)