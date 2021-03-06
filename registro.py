# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Registro(object):
    def setupUi(self, Registro):
        if not Registro.objectName():
            Registro.setObjectName(u"Registro")
        Registro.resize(459, 299)
        self.gridLayout = QGridLayout(Registro)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LecturaTab = QTabWidget(Registro)
        self.LecturaTab.setObjectName(u"LecturaTab")
        self.RegistroTab = QWidget()
        self.RegistroTab.setObjectName(u"RegistroTab")
        self.gridLayout_2 = QGridLayout(self.RegistroTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.AceptarPB = QPushButton(self.RegistroTab)
        self.AceptarPB.setObjectName(u"AceptarPB")

        self.gridLayout_2.addWidget(self.AceptarPB, 8, 0, 1, 5)

        self.MostrarPB = QPushButton(self.RegistroTab)
        self.MostrarPB.setObjectName(u"MostrarPB")
        self.MostrarPB.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.MostrarPB, 4, 4, 1, 1)

        self.NombreLE = QLineEdit(self.RegistroTab)
        self.NombreLE.setObjectName(u"NombreLE")

        self.gridLayout_2.addWidget(self.NombreLE, 0, 2, 1, 2)

        self.MateriasLE = QLineEdit(self.RegistroTab)
        self.MateriasLE.setObjectName(u"MateriasLE")

        self.gridLayout_2.addWidget(self.MateriasLE, 5, 2, 1, 2)

        self.CorreoLE = QLineEdit(self.RegistroTab)
        self.CorreoLE.setObjectName(u"CorreoLE")

        self.gridLayout_2.addWidget(self.CorreoLE, 1, 2, 1, 2)

        self.ContrasenaLE = QLineEdit(self.RegistroTab)
        self.ContrasenaLE.setObjectName(u"ContrasenaLE")
        self.ContrasenaLE.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.ContrasenaLE, 4, 2, 1, 2)

        self.NombreL = QLabel(self.RegistroTab)
        self.NombreL.setObjectName(u"NombreL")

        self.gridLayout_2.addWidget(self.NombreL, 0, 1, 1, 1)

        self.CorreoL = QLabel(self.RegistroTab)
        self.CorreoL.setObjectName(u"CorreoL")

        self.gridLayout_2.addWidget(self.CorreoL, 1, 1, 1, 1)

        self.ContasenaL = QLabel(self.RegistroTab)
        self.ContasenaL.setObjectName(u"ContasenaL")

        self.gridLayout_2.addWidget(self.ContasenaL, 4, 1, 1, 1)

        self.MateriasL = QLabel(self.RegistroTab)
        self.MateriasL.setObjectName(u"MateriasL")

        self.gridLayout_2.addWidget(self.MateriasL, 5, 1, 1, 1)

        self.LecturaTab.addTab(self.RegistroTab, "")
        self.EditarTab = QWidget()
        self.EditarTab.setObjectName(u"EditarTab")
        self.NombreEditL = QLabel(self.EditarTab)
        self.NombreEditL.setObjectName(u"NombreEditL")
        self.NombreEditL.setGeometry(QRect(30, 20, 55, 16))
        self.NombreEditLE = QLineEdit(self.EditarTab)
        self.NombreEditLE.setObjectName(u"NombreEditLE")
        self.NombreEditLE.setGeometry(QRect(100, 20, 211, 22))
        self.line = QFrame(self.EditarTab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 591, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.AceptarEditLE = QPushButton(self.EditarTab)
        self.AceptarEditLE.setObjectName(u"AceptarEditLE")
        self.AceptarEditLE.setGeometry(QRect(10, 210, 411, 28))
        self.label_11 = QLabel(self.EditarTab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 60, 141, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.layoutWidget = QWidget(self.EditarTab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 90, 411, 119))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.CorreoEditLE = QLineEdit(self.layoutWidget)
        self.CorreoEditLE.setObjectName(u"CorreoEditLE")

        self.gridLayout_3.addWidget(self.CorreoEditLE, 1, 1, 1, 1)

        self.NombreEdit2L = QLabel(self.layoutWidget)
        self.NombreEdit2L.setObjectName(u"NombreEdit2L")

        self.gridLayout_3.addWidget(self.NombreEdit2L, 0, 0, 1, 1)

        self.CorreoEditL = QLabel(self.layoutWidget)
        self.CorreoEditL.setObjectName(u"CorreoEditL")

        self.gridLayout_3.addWidget(self.CorreoEditL, 1, 0, 1, 1)

        self.MateriasEditL = QLabel(self.layoutWidget)
        self.MateriasEditL.setObjectName(u"MateriasEditL")

        self.gridLayout_3.addWidget(self.MateriasEditL, 3, 0, 1, 1)

        self.MateriasEditLE = QLineEdit(self.layoutWidget)
        self.MateriasEditLE.setObjectName(u"MateriasEditLE")

        self.gridLayout_3.addWidget(self.MateriasEditLE, 3, 1, 1, 1)

        self.ContrasenaEditLE = QLineEdit(self.layoutWidget)
        self.ContrasenaEditLE.setObjectName(u"ContrasenaEditLE")

        self.gridLayout_3.addWidget(self.ContrasenaEditLE, 2, 1, 1, 1)

        self.ContrasenaEditL = QLabel(self.layoutWidget)
        self.ContrasenaEditL.setObjectName(u"ContrasenaEditL")

        self.gridLayout_3.addWidget(self.ContrasenaEditL, 2, 0, 1, 1)

        self.NombreEdit2LE = QLineEdit(self.layoutWidget)
        self.NombreEdit2LE.setObjectName(u"NombreEdit2LE")

        self.gridLayout_3.addWidget(self.NombreEdit2LE, 0, 1, 1, 1)

        self.NomCB = QCheckBox(self.layoutWidget)
        self.NomCB.setObjectName(u"NomCB")

        self.gridLayout_3.addWidget(self.NomCB, 0, 2, 1, 1)

        self.CorrCB = QCheckBox(self.layoutWidget)
        self.CorrCB.setObjectName(u"CorrCB")

        self.gridLayout_3.addWidget(self.CorrCB, 1, 2, 1, 1)

        self.ContCB = QCheckBox(self.layoutWidget)
        self.ContCB.setObjectName(u"ContCB")

        self.gridLayout_3.addWidget(self.ContCB, 2, 2, 1, 1)

        self.MateriasCB = QCheckBox(self.layoutWidget)
        self.MateriasCB.setObjectName(u"MateriasCB")

        self.gridLayout_3.addWidget(self.MateriasCB, 3, 2, 1, 1)

        self.LecturaTab.addTab(self.EditarTab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.MostrarPB_2 = QPushButton(self.tab)
        self.MostrarPB_2.setObjectName(u"MostrarPB_2")
        self.MostrarPB_2.setGeometry(QRect(320, 0, 93, 28))
        self.MensajeTE = QTextEdit(self.tab)
        self.MensajeTE.setObjectName(u"MensajeTE")
        self.MensajeTE.setGeometry(QRect(0, 30, 431, 221))
        self.LecturaTab.addTab(self.tab, "")
        self.EliminarTab = QWidget()
        self.EliminarTab.setObjectName(u"EliminarTab")
        self.NombreElimL = QLabel(self.EliminarTab)
        self.NombreElimL.setObjectName(u"NombreElimL")
        self.NombreElimL.setGeometry(QRect(20, 40, 55, 16))
        self.NombreElimLE = QLineEdit(self.EliminarTab)
        self.NombreElimLE.setObjectName(u"NombreElimLE")
        self.NombreElimLE.setGeometry(QRect(90, 40, 221, 22))
        self.ElimTodosRB = QRadioButton(self.EliminarTab)
        self.ElimTodosRB.setObjectName(u"ElimTodosRB")
        self.ElimTodosRB.setGeometry(QRect(20, 110, 181, 20))
        self.AceptarElimPB = QPushButton(self.EliminarTab)
        self.AceptarElimPB.setObjectName(u"AceptarElimPB")
        self.AceptarElimPB.setGeometry(QRect(10, 200, 321, 28))
        self.LecturaTab.addTab(self.EliminarTab, "")

        self.gridLayout.addWidget(self.LecturaTab, 1, 0, 1, 1)


        self.retranslateUi(Registro)

        self.LecturaTab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Registro)
    # setupUi

    def retranslateUi(self, Registro):
        Registro.setWindowTitle(QCoreApplication.translate("Registro", u"Registro de estudiantes", None))
        self.AceptarPB.setText(QCoreApplication.translate("Registro", u"Aceptar", None))
        self.MostrarPB.setText(QCoreApplication.translate("Registro", u"Mostrar", None))
        self.NombreLE.setText("")
        self.NombreL.setText(QCoreApplication.translate("Registro", u"Nombre", None))
        self.CorreoL.setText(QCoreApplication.translate("Registro", u"Correo", None))
        self.ContasenaL.setText(QCoreApplication.translate("Registro", u"Contrase\u00f1a", None))
        self.MateriasL.setText(QCoreApplication.translate("Registro", u"Materias", None))
        self.LecturaTab.setTabText(self.LecturaTab.indexOf(self.RegistroTab), QCoreApplication.translate("Registro", u"Registro", None))
        self.NombreEditL.setText(QCoreApplication.translate("Registro", u"Nombre", None))
        self.AceptarEditLE.setText(QCoreApplication.translate("Registro", u"Aceptar", None))
        self.label_11.setText(QCoreApplication.translate("Registro", u"Campos a editar", None))
        self.NombreEdit2L.setText(QCoreApplication.translate("Registro", u"Nombre", None))
        self.CorreoEditL.setText(QCoreApplication.translate("Registro", u"Correo", None))
        self.MateriasEditL.setText(QCoreApplication.translate("Registro", u"Materias", None))
        self.ContrasenaEditL.setText(QCoreApplication.translate("Registro", u"Contrase\u00f1a", None))
        self.NomCB.setText("")
        self.CorrCB.setText("")
        self.ContCB.setText("")
        self.MateriasCB.setText("")
        self.LecturaTab.setTabText(self.LecturaTab.indexOf(self.EditarTab), QCoreApplication.translate("Registro", u"Editar", None))
        self.MostrarPB_2.setText(QCoreApplication.translate("Registro", u"Mostrar", None))
        self.LecturaTab.setTabText(self.LecturaTab.indexOf(self.tab), QCoreApplication.translate("Registro", u"Alumnos", None))
        self.NombreElimL.setText(QCoreApplication.translate("Registro", u"Nombre", None))
        self.ElimTodosRB.setText(QCoreApplication.translate("Registro", u"Eliminar todos los alumnos", None))
        self.AceptarElimPB.setText(QCoreApplication.translate("Registro", u"Aceptar", None))
        self.LecturaTab.setTabText(self.LecturaTab.indexOf(self.EliminarTab), QCoreApplication.translate("Registro", u"Eliminar", None))
    # retranslateUi

