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
        self.titulo = "tomara que vai"

        self.label_1 = QLabel(self)
        self.label_2 = QLabel(self)

        self.caixa_texto = QLineEdit(self)  # caixa de texto
        self.caixa_texto.move(20,25)
        self.caixa_texto.resize(250,50)

        self.caixa_texto_2 = QLineEdit(self)  # caixa de texto descriptografia
        self.caixa_texto_2.move(120,400)
        self.caixa_texto_2.resize(500,50)
        
        self.label_2.move(120,350)
        self.label_2.setStyleSheet('QLabel{font: bold; font-size:20px}')
        self.label_2.resize(590,50)
        self.label_2.setText("A mensagens descriptografadas apareceram aqui")

        botao1 = QPushButton('LIMPAR', self)
        botao1.move(20,100)
        botao1.resize(150,80)
        botao1.setStyleSheet('QPushButton {background-color:#FFF; font: bold; font-size:20px}')
        botao1.clicked.connect(self.limpar)
        
        botao_md5 = QPushButton('MD5', self)
        botao_md5.move(20,200)
        botao_md5.resize(150,80)
        botao_md5.setStyleSheet('QPushButton {background-color:#FFF; font: bold; font-size:20px}')
        botao_md5.clicked.connect(self.md5)

        botao_sha_1 = QPushButton('SHA_1', self)
        botao_sha_1.move(170,200)
        botao_sha_1.resize(150,80)
        botao_sha_1.setStyleSheet('QPushButton {background-color:#FFF; font: bold; font-size:20px}')
        botao_sha_1.clicked.connect(self.sha_1)

        botao_sha_2 = QPushButton('SHA_2', self)
        botao_sha_2.move(320,200)
        botao_sha_2.resize(150,80)
        botao_sha_2.setStyleSheet('QPushButton {background-color:#FFF; font: bold; font-size:20px}')
        botao_sha_2.clicked.connect(self.sha_2)

        botao_sha_3 = QPushButton('SHA_3', self)
        botao_sha_3.move(470,200)
        botao_sha_3.resize(150,80)
        botao_sha_3.setStyleSheet('QPushButton {background-color:#FFF; font: bold; font-size:20px}')
        botao_sha_3.clicked.connect(self.sha_3)

        self.label_1 = QLabel(self)
        self.label_1.move(300,30)
        self.label_1.setStyleSheet('QLabel{font: bold; font-size:20px}')
        self.label_1.resize(500,50)
        self.label_1.setText("Limpe a caixa a cada teste")

        self.CarregarJanela()
        
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def limpar(self):
        self.caixa_texto.setText('')
        self.caixa_texto_2.setText('')

    def md5(self):
        conteudo_caixa = self.caixa_texto.text()
        resultado = hashlib.md5(conteudo_caixa.encode('UTF-8')).hexdigest()
        self.caixa_texto_2.setText(resultado)

    def sha_1(self):
        conteudo_caixa = self.caixa_texto.text()
        resultado = hashlib.sha1(conteudo_caixa.encode('UTF-8')).hexdigest()
        self.caixa_texto_2.setText(resultado)
    
    def sha_2(self):
        conteudo_caixa = self.caixa_texto.text()
        resultado = hashlib.sha256(conteudo_caixa.encode('UTF-8')).hexdigest()
        self.caixa_texto_2.setText(resultado)
    
    def sha_3(self):
        conteudo_caixa = self.caixa_texto.text()
        resultado = hashlib.sha3_256(conteudo_caixa.encode('UTF-8')).hexdigest()
        self.caixa_texto_2.setText(resultado)
    
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())

help(sys)
