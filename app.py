import os, sys, subprocess
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap

class ejemplo_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.outputt.setEnabled(False)
        self.instalar_boton.clicked.connect(self.instalar)
        self.desinstalar_boton.clicked.connect(self.desinstalar)
        self.lista.clicked.connect(self.librerias)

    def instalar(self):
        libreria = self.texto.text()
        comando = "pip install " + libreria
        os.system(comando)
        self.resultado.setText("Hecho")
    def desinstalar(self):
        libreria = self.texto.text()
        comando = "pip uninstall " + libreria
        os.system(comando)
        self.resultado.setText("Hecho")
    def librerias(self):
        comando = "pip list"
        output = subprocess.check_output(comando, shell=True)
        self.outputt.setEnabled(True)
        outputR = (output.decode("utf-8"))
        self.outputt.setText(outputR)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    GUI.setWindowTitle("pip installer by M.D.W")
    GUI.setWindowIcon(QtGui.QIcon('icon.png'))
    sys.exit(app.exec_())

