from PySide2.QtUiTools import QUiLoader     #Esta se agregó
from PySide2.QtCore import QFile    #Esta se agregó
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from registro import *
import sys
from mongoengine import *
from StudentsIO import *
from mongoengine import *
from pymongo import MongoClient

connect('IECA', host = 'localhost', port = 27017)

class Registro(QMainWindow):
    def __init__(self):
        super(Registro, self).__init__()
        self.ui = QUiLoader().load(QFile("registro.ui"))

# ----------------Registro---------------
        self.ui.MostrarPB.clicked.connect(self.mostrarPassword)
        self.ui.AceptarPB.clicked.connect(self.aceptarRegistro)

# ----------------Edición---------------
        self.ui.AceptarEditLE.clicked.connect(self.aceptarEdicion)

# ----------------Visualización---------
        self.ui.MostrarPB_2.clicked.connect(self.visualizarTabla)
# ----------------Eliminar---------------
        self.ui.AceptarElimPB.clicked.connect(self.Eliminar)

###################################################################################
#----------------Registro---------------
    def mostrarPassword(self):

        if self.ui.ContrasenaLE.echoMode() == QLineEdit.Normal:
            self.ui.ContrasenaLE.setEchoMode(QLineEdit.Password)
            self.ui.MostrarPB.setText('Mostrar')
        else:
            self.ui.ContrasenaLE.setEchoMode(QLineEdit.Normal)
            self.ui.MostrarPB.setText('Ocultar')

    def aceptarRegistro(self):
        nombre = self.ui.NombreLE.text()
        correo = self.ui.CorreoLE.text()
        psw = self.ui.ContrasenaLE.text()
        materias = self.ui.MateriasLE.text()
        writeNew_estudiante(nombre,correo,psw,materias)
        print(nombre)
        self.ui.NombreLE.clear()
        self.ui.CorreoLE.clear()
        self.ui.ContrasenaLE.clear()
        self.ui.MateriasLE.clear()

#----------------Edición---------------
    def aceptarEdicion(self):
        nome = self.ui.NombreEditLE.text()
        nombre = self.ui.NombreEdit2LE.text()
        n = self.ui.NomCB.isChecked()
        correo = self.ui.CorreoEditLE.text()
        cr =self.ui.CorrCB.isChecked()
        psw = self.ui.ContrasenaEditLE.text()
        cn =self.ui.ContCB.isChecked()
        materias = self.ui.MateriasEditLE.text()
        mt =self.ui.MateriasCB.isChecked()
        edit_estudiante(nome,nombre,n,correo,cr,psw,cn,materias,mt)
        self.ui.NombreEditLE.clear()
        self.ui.CorreoEditLE.clear()
        self.ui.ContrasenaEditLE.clear()
        self.ui.MateriasEditLE.clear()

# ----------------Visualización--------
    def visualizarTabla(self):
        client = MongoClient('localhost', 27017)
        db = client['IECA']
        coll = db['estudiante']
        for a in Estudiante.objects:
            self.ui.MensajeTE.append(f'Nombre: {a.Nombre}')
            self.ui.MensajeTE.append(f'Correo: {a.Correo}')
            self.ui.MensajeTE.append(f'Contraseña: {a.Contrasena}')
            self.ui.MensajeTE.append(f'Materias: {a.Materias}')
            self.ui.MensajeTE.append('-------------------------------------------------------')

#----------------Eliminar---------------
    def Eliminar(self):
        deleteOne(self.ui.NombreElimLE.text())
        self.ui.NombreElimLE.clear()

        if self.ui.ElimTodosRB.isChecked():
            delete_All()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Registro()
    window.ui.show()
    sys.exit(app.exec_())