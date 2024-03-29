# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fiche_Film.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Ecran_Choix import Ui_Choix




class Ui_Fiche_Film(object):

    def setupUi(self, Fiche_Film):



        def affiche_choix():
            
            #Construction Fiche Film
            #import sys
            #app = QtWidgets.QApplication(sys.argv)
            Choix_seance = QtWidgets.QMainWindow()
            seance = Ui_Choix()
            seance.setupUi(Choix_seance)
            
            Choix_seance.show()

        Fiche_Film.setObjectName("Fiche_Film")
        Fiche_Film.resize(623, 597)
        Fiche_Film.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Fiche_Film)
        self.centralwidget.setObjectName("centralwidget")
        self.Titre = QtWidgets.QLabel(self.centralwidget)
        self.Titre.setGeometry(QtCore.QRect(20, 0, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Titre.setFont(font)
        self.Titre.setAlignment(QtCore.Qt.AlignCenter)
        self.Titre.setObjectName("Titre")
        self.Titre.setStyleSheet("color: white")
        self.Affiche_Film = QtWidgets.QLabel(self.centralwidget)
        self.Affiche_Film.setGeometry(QtCore.QRect(20, 50, 261, 331))
        self.Affiche_Film.setFrameShape(QtWidgets.QFrame.Panel)
        self.Affiche_Film.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Affiche_Film.setText("")
        self.Affiche_Film.setObjectName("Affiche_Film")
        self.label_synopsis = QtWidgets.QLabel(self.centralwidget)
        self.label_synopsis.setGeometry(QtCore.QRect(310, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_synopsis.setFont(font)
        self.label_synopsis.setObjectName("label_synopsis")
        self.label_synopsis.setStyleSheet("color: white")
        self.Text_Synopsis = QtWidgets.QLabel(self.centralwidget)
        self.Text_Synopsis.setGeometry(QtCore.QRect(310, 70, 301, 121))
        self.Text_Synopsis.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Text_Synopsis.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Text_Synopsis.setWordWrap(True)
        self.Text_Synopsis.setObjectName("Text_Synopsis")
        self.Text_Synopsis.setStyleSheet("color: white")
        self.label_Genre = QtWidgets.QLabel(self.centralwidget)
        self.label_Genre.setGeometry(QtCore.QRect(310, 200, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Genre.setFont(font)
        self.label_Genre.setObjectName("label_Genre")
        self.label_Genre.setStyleSheet("color: white")
        self.Text_Genre = QtWidgets.QLabel(self.centralwidget)
        self.Text_Genre.setGeometry(QtCore.QRect(310, 220, 301, 81))
        self.Text_Genre.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Text_Genre.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Text_Genre.setWordWrap(True)
        self.Text_Genre.setObjectName("Text_Genre")
        self.Text_Genre.setStyleSheet("color: white")
        self.label_Acteur = QtWidgets.QLabel(self.centralwidget)
        self.label_Acteur.setGeometry(QtCore.QRect(310, 300, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Acteur.setFont(font)
        self.label_Acteur.setObjectName("label_Acteur")
        self.label_Acteur.setStyleSheet("color: white")
        self.Text_Genre_2 = QtWidgets.QLabel(self.centralwidget)
        self.Text_Genre_2.setGeometry(QtCore.QRect(310, 320, 301, 81))
        self.Text_Genre_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Text_Genre_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Text_Genre_2.setWordWrap(True)
        self.Text_Genre_2.setObjectName("Text_Genre_2")
        self.Text_Genre_2.setStyleSheet("color: white")
        self.label_Duree = QtWidgets.QLabel(self.centralwidget)
        self.label_Duree.setGeometry(QtCore.QRect(310, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Duree.setFont(font)
        self.label_Duree.setObjectName("label_Duree")
        self.label_Duree.setStyleSheet("color: white")
        self.Text_Duree = QtWidgets.QLabel(self.centralwidget)
        self.Text_Duree.setGeometry(QtCore.QRect(400, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Text_Duree.setFont(font)
        self.Text_Duree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Text_Duree.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Text_Duree.setWordWrap(False)
        self.Text_Duree.setObjectName("Text_Duree")
        self.Text_Duree.setStyleSheet("color: white")
        self.Seances = QtWidgets.QLabel(self.centralwidget)
        self.Seances.setGeometry(QtCore.QRect(10, 390, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Seances.setFont(font)
        self.Seances.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Seances.setObjectName("Seances")
        self.Seances.setStyleSheet("color: white")
        self.PB_Seance1 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_Seance1.setGeometry(QtCore.QRect(10, 430, 111, 61))
        self.PB_Seance1.setObjectName("PB_Seance1")
        self.PB_Seance1.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.PB_Seance1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_Seance1_2.setGeometry(QtCore.QRect(130, 430, 111, 61))
        self.PB_Seance1_2.setObjectName("PB_Seance1_2")
        self.PB_Seance1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_Seance1_3.setGeometry(QtCore.QRect(250, 430, 111, 61))
        self.PB_Seance1_3.setObjectName("PB_Seance1_3")
        self.PB_Seance1_4 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_Seance1_4.setGeometry(QtCore.QRect(370, 430, 111, 61))
        self.PB_Seance1_4.setObjectName("PB_Seance1_4")
    # self.ReturnButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ReturnButton.setGeometry(QtCore.QRect(520, 0, 101, 41))
        self.ReturnButton.setObjectName("ReturnButton")
        self.ReturnButton.setStyleSheet("color: white")
        self.ReturnButton.clicked.connect(Fiche_Film.hide)
        Fiche_Film.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Fiche_Film)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 21))
        self.menubar.setObjectName("menubar")
        Fiche_Film.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Fiche_Film)
        self.statusbar.setObjectName("statusbar")
        Fiche_Film.setStatusBar(self.statusbar)

        self.retranslateUi(Fiche_Film)
        QtCore.QMetaObject.connectSlotsByName(Fiche_Film)


    def retranslateUi(self, Fiche_Film):
        _translate = QtCore.QCoreApplication.translate
        Fiche_Film.setWindowTitle(_translate("Fiche_Film", "Fiche Film"))
        self.Titre.setText(_translate("Fiche_Film", "FILM"))
        self.label_synopsis.setText(_translate("Fiche_Film", "Synopsis"))
        self.label_Genre.setText(_translate("Fiche_Film", "Genre"))
        self.label_Acteur.setText(_translate("Fiche_Film", "Acteurs"))
        self.label_Duree.setText(_translate("Fiche_Film", "Durée"))
        self.Seances.setText(_translate("Fiche_Film", "Séances"))
        self.ReturnButton.setText(_translate("Fiche_Film", "Accueil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fiche_Film = QtWidgets.QWidget ()
    ui = Ui_Fiche_Film()
    ui.setupUi(Fiche_Film)
    Fiche_Film.show()
    sys.exit(app.exec_())
