import os, sys, subprocess,platform,time
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap

def test_py_fn():
    test_py = subprocess.check_output("python --version")
    test_py = (test_py.decode("utf-8"))
    if list(test_py)[7] == "3":
        x = "pip3"
    elif list(test_py)[7] == "2":
        x = "pip2"
    else:
        test_py = subprocess.check_output("python2 --version")
        test_py = (test_py.decode("utf-8"))
        if list(test_py)[7] == "2":
            x = "pip2"
        else:
            test_py = subprocess.check_output("python3 --version")
            test_py = (test_py.decode("utf-8"))
            if list(test_py)[7] == "3":
                x = "pip3"
            else:
                if platform.system() == "Windows":
                    com = "start File_Error.txt"
                    os.system(com)
                    exit()
                elif platform.system() == "Linux":
                    com = "apt install python3"
                    os.system(com)
                    time.sleep(2)



class ejemplo_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.outputt.setEnabled(False)
        self.instalar_boton.clicked.connect(self.instalar)
        self.desinstalar_boton.clicked.connect(self.desinstalar)
        self.lista.clicked.connect(self.librerias)

    def instalar(self,x):
        libreria = self.texto.text()
        comando = x + " install " + libreria
        os.system(comando)
        self.resultado.setText("Hecho")
    def desinstalar(self,x):
        libreria = self.texto.text()
        comando = x + " uninstall " + libreria
        os.system(comando)
        self.resultado.setText("Hecho")
    def librerias(self,x):
        comando = x + " list"
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

