# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ecran_Principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EcranPrincipal(object):
    

    
    def setupUi(self, EcranPrincipal):
        
       #Convertir les images
        def pixmap_image(image):
        
            #Lieu de stockage des images
            repertoire = "C:\\Users\\Elise\\Desktop\\2022 - 2023 année première\\NSI\\projet4_papa\\images\\"
            file = str(repertoire) + str(image)

            #Conversion des Affiche en icon pour les boutons et en Pixmap pour la grande affiche
            return QtGui.QPixmap(file)         
        
        
        
        EcranPrincipal.setObjectName("EcranPrincipal")
        EcranPrincipal.resize(617, 593)
        EcranPrincipal.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(EcranPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white")
        
        #Conversion des Affiche en icon pour les boutons et en Pixmap pour la grande affiche
        Pixmap_Film1 = pixmap_image("AntMan.jpg")
        ButtonIcon1 = QtGui.QIcon(Pixmap_Film1)
        Pixmap_Film2 = pixmap_image("Creed.jpg")
        ButtonIcon2 = QtGui.QIcon(Pixmap_Film2)
        Pixmap_Film3 = pixmap_image("Seoul.jpg")
        ButtonIcon3 = QtGui.QIcon(Pixmap_Film3)
        Pixmap_Film4 = pixmap_image("Galaxie.jpg")
        ButtonIcon4 = QtGui.QIcon(Pixmap_Film4)
        Pixmap_Film5 = pixmap_image("Elemental.jpg")
        ButtonIcon5 = QtGui.QIcon(Pixmap_Film5)
        Pixmap_Film6 = pixmap_image("AntMan_Grand.jpg")

        
        self.Affiche = QtWidgets.QLabel(self.centralwidget)
        self.Affiche.setGeometry(QtCore.QRect(90, 50, 451, 281))
        self.Affiche.setFrameShape(QtWidgets.QFrame.Panel)
        self.Affiche.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Affiche.setText("")
        self.Affiche.setObjectName("Affiche")
        self.Affiche.setPixmap(Pixmap_Film6)
        
        self.Label_1 = QtWidgets.QLabel(self.centralwidget)
        self.Label_1.setGeometry(QtCore.QRect(10, 340, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Label_1.setFont(font)
        self.Label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Label_1.setObjectName("Label_1")
        self.Label_1.setStyleSheet("color: white")

        

        
        self.PB_Film1 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_Film1.setGeometry(QtCore.QRect(10, 370, 111, 161))
        self.PB_Film1.setText("")
        self.PB_Film1.setObjectName("PB_Film1")
        self.PB_Film1.setIcon(ButtonIcon1)
        self.PB_Film1.setIconSize(Pixmap_Film1.rect().size())
        self.PB_Film1.repaint()
        
        self.PB_Film1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_Film1_2.setGeometry(QtCore.QRect(130, 370, 111, 161))
        self.PB_Film1_2.setText("")
        self.PB_Film1_2.setObjectName("PB_Film1_2")
        self.PB_Film1_2.setIcon(ButtonIcon2)
        self.PB_Film1_2.setIconSize(Pixmap_Film2.rect().size())
        self.PB_Film1_2.repaint()
        
        self.PB_Film1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_Film1_3.setGeometry(QtCore.QRect(250, 370, 111, 161))
        self.PB_Film1_3.setText("")
        self.PB_Film1_3.setObjectName("PB_Film1_3")
        self.PB_Film1_3.setIcon(ButtonIcon3)
        self.PB_Film1_3.setIconSize(Pixmap_Film3.rect().size())
        self.PB_Film1_3.repaint()

        
        self.PB_Film1_4 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_Film1_4.setGeometry(QtCore.QRect(370, 370, 111, 161))
        self.PB_Film1_4.setText("")
        self.PB_Film1_4.setObjectName("PB_Film1_4")
        self.PB_Film1_4.setIcon(ButtonIcon4)
        self.PB_Film1_4.setIconSize(Pixmap_Film4.rect().size())
        self.PB_Film1_4.repaint()

        
        self.PB_Film1_5 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_Film1_5.setGeometry(QtCore.QRect(490, 370, 111, 161))
        self.PB_Film1_5.setText("")
        self.PB_Film1_5.setObjectName("PB_Film1_5")
        self.PB_Film1_5.setIcon(ButtonIcon5)
        self.PB_Film1_5.setIconSize(Pixmap_Film5.rect().size())
        self.PB_Film1_5.repaint()

        
        EcranPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EcranPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 21))
        self.menubar.setObjectName("menubar")
        EcranPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EcranPrincipal)
        self.statusbar.setObjectName("statusbar")
        EcranPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(EcranPrincipal)
        QtCore.QMetaObject.connectSlotsByName(EcranPrincipal)

    def retranslateUi(self, EcranPrincipal):
        _translate = QtCore.QCoreApplication.translate
        EcranPrincipal.setWindowTitle(_translate("EcranPrincipal", "Reserver votre séance"))
        self.label.setText(_translate("EcranPrincipal", "CineFlash"))# nom du cinéma
        self.Label_1.setText(_translate("EcranPrincipal", "A l\'affiche"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EcranPrincipal = QtWidgets.QMainWindow()
    ui = Ui_EcranPrincipal()
    ui.setupUi(EcranPrincipal)
    EcranPrincipal.show()
    sys.exit(app.exec_())
