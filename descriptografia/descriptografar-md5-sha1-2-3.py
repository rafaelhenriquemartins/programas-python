import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip,QLabel, QLineEdit
# MD4, MD5, SHA-1, SHA-2 e SHA-3
import hashlib

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.altura = 600
        self.largura = 800
        self.titulo = "Tomara que vai"
        

        self.label_1 = QLabel(self)
        self.label_2 = QLabel(self)

        self.caixa_texto = QLineEdit(self)  # caixa de texto
        self.caixa_texto.setText('')
        self.caixa_texto.move(20,25)
        self.caixa_texto.resize(600,200)
        self.caixa_texto.setStyleSheet('QLineEdit{font-size:20px; border:1px solid black}')

        self.caixa_texto_input = QLineEdit(self)  # caixa de texto
        self.caixa_texto_input.move(280,27)
        self.caixa_texto_input.resize(150,50)
        self.caixa_texto_input.setStyleSheet('QLineEdit{font-size:20px; border:-2px solid black}')
        self.caixa_texto_input.setText('Input')
        self.caixa_texto_input.setDisabled(True)

        self.caixa_texto_2 = QLineEdit(self)  # caixa de texto descriptografia
        self.caixa_texto_2.setText('')
        self.caixa_texto_2.move(20,300)
        self.caixa_texto_2.resize(600,200)
        self.caixa_texto_2.setStyleSheet('QLineEdit{font-size:15px;border:1px solid black}')

        self.caixa_texto_output = QLineEdit(self)  # caixa de texto
        self.caixa_texto_output.move(280,302)
        self.caixa_texto_output.resize(150,50)
        self.caixa_texto_output.setStyleSheet('QLineEdit{font-size:20px; border:-2px solid black}')
        self.caixa_texto_output.setText('Output')
        self.caixa_texto_output.setDisabled(True)

        self.caixa_texto_funcao = QLineEdit(self)  # caixa de texto
        self.caixa_texto_funcao.move(450,302)
        self.caixa_texto_funcao.resize(150,50)
        self.caixa_texto_funcao.setStyleSheet('QLineEdit{font-size:20px; border:-2px solid black}')
        self.caixa_texto_funcao.setDisabled(True)

        botao1 = QPushButton('LIMPAR', self)
        botao1.move(235,240)
        botao1.resize(150,40)
        botao1.setStyleSheet('QPushButton {background-color:#FFF; font: bold; font-size:20px}')
        botao1.clicked.connect(self.limpar)

        botao_md5 = QPushButton('MD5', self)
        botao_md5.move(635,40)
        botao_md5.resize(150,80)
        botao_md5.setStyleSheet('QPushButton {background-color:#FFF; font: bold; font-size:20px}')
        botao_md5.clicked.connect(self.md5)

        botao_sha_1 = QPushButton('SHA_1', self)
        botao_sha_1.move(635,120)
        botao_sha_1.resize(150,80)
        botao_sha_1.setStyleSheet('QPushButton {background-color:#FFF; font: bold; font-size:20px}')
        botao_sha_1.clicked.connect(self.sha_1)

        botao_sha_2 = QPushButton('SHA256', self)
        botao_sha_2.move(635,200)
        botao_sha_2.resize(150,80)
        botao_sha_2.setStyleSheet('QPushButton {background-color:#FFF; font: bold; font-size:20px}')
        botao_sha_2.clicked.connect(self.sha_2)

        botao_sha_3 = QPushButton('SHA3_256', self)
        botao_sha_3.move(635,280)
        botao_sha_3.resize(150,80)
        botao_sha_3.setStyleSheet('QPushButton {background-color:#FFF; font: bold; font-size:20px; }')
        botao_sha_3.clicked.connect(self.sha_3)

        self.label_1 = QLabel(self)
        self.label_1.move(680,0)
        self.label_1.setStyleSheet('QLabel{font: bold; font-size:20px}')
        self.label_1.resize(80,50)
        self.label_1.setText("HASH")

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def limpar(self):
        self.caixa_texto.setText('')
        self.caixa_texto_2.setText('')
        self.caixa_texto_funcao.setText('')

    def md5(self):       
        conteudo_caixa = self.caixa_texto.text()
        resultado = hashlib.md5(conteudo_caixa.encode('UTF-8')).hexdigest()
        self.caixa_texto_2.setText('                                 ' + resultado)
        self.caixa_texto_funcao.setText('')
        self.caixa_texto_funcao.setText('MD5')
            
    def sha_1(self):
        conteudo_caixa = self.caixa_texto.text()
        resultado = hashlib.sha1(conteudo_caixa.encode('UTF-8')).hexdigest()
        self.caixa_texto_2.setText('                          ' + resultado)
        self.caixa_texto_funcao.setText('')
        self.caixa_texto_funcao.setText('SHA_1')

    def sha_2(self): #sha256
        conteudo_caixa = self.caixa_texto.text()
        resultado = hashlib.sha256(conteudo_caixa.encode('UTF-8')).hexdigest()
        self.caixa_texto_2.setText('        ' + resultado)
        self.caixa_texto_funcao.setText('')
        self.caixa_texto_funcao.setText('SHA256')

    def sha_3(self):#sha3_256
        conteudo_caixa = self.caixa_texto.text()
        resultado = hashlib.sha3_256(conteudo_caixa.encode('UTF-8')).hexdigest()
        self.caixa_texto_2.setText('        ' + resultado)
        self.caixa_texto_funcao.setText('')
        self.caixa_texto_funcao.setText('SHA3_256')

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())