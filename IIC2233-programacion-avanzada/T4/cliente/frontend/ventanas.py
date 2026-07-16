from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QApplication,
                            QLineEdit, QVBoxLayout, QApplication)
import sys


class VentanaInicial(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, *kwargs)
        self.init_gui()
        self.show()

    #https://doc.qt.io/qt-6/stylesheet-examples.html
    #estilos y ayudas https://www.youtube.com/watch?v=735dNm-ar_0
    def init_gui(self) -> None:
        self.setGeometry(0, 0, 1080, 720)
        self.setStyleSheet("background-color: #0095FF;")
        self.setWindowTitle('DCCaída de palabras')
        
        self.label1 = QLabel("¡BIENVENIDO A DCCAÍDA DE PALABRAS!")
        self.label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter )
        self.label1.setFont(QFont("Cascadia Code", 40))
        self.label1.setStyleSheet("font-style: italic;"
                                "border: 5px solid black;")
        
        self.label2 = QLabel("🤓")
        self.label2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter )
        self.label2.setFont(QFont("Cascadia Code", 60))
        
        self.label3 = QLabel('ingresa tu nombre:', self)
        self.label3.setFont(QFont("Cascadia Code", 16))
        self.label3.setStyleSheet("font-style: italic;")
        
        self.edit1 = QLineEdit('', self)
        self.edit1.resize(100, 20)
        self.edit1.setFont(QFont("Cascadia Code", 16))
        self.edit1.setStyleSheet("background-color: white;"
                                "font-style: italic;")
        
        self.boton1 = QPushButton('&iniciar', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.setFont(QFont("Cascadia Code", 16))
        self.boton1.setStyleSheet("background-color: white;"
                                "font-style: italic;")

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addStretch(1)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addStretch(1)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.edit1)
        vbox.addWidget(self.boton1)
        vbox.addStretch(1)
        self.setLayout(vbox)
        self.center()
    #codigo sacado de https://stackoverflow.com/questions/20243637/pyqt4-center-window-on-active-screen
    #centrar automatico cuando se abre la pantalla y mover con el mouse
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())



if __name__ == '__main__':

    app = QApplication([])  
    ventana = VentanaInicial()   
    ventana.show()          
    sys.exit(app.exec())    


