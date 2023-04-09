# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\moleres\Documents\GitHub\projet-4-cinoche\nombre_place.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_nombre_place(object):
    def setupUi(self, nombre_place):
        nombre_place.setObjectName("nombre_place")
        nombre_place.resize(502, 400)
        font_titre= QtGui.QFont()
        font_titre.setFamily("Arial Black")
        font_titre.setPointSize(20)
        font_titre.setBold(True)
        font_titre.setWeight(75)
        
        font= QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(10)
        
        self.gridLayout_2 = QtWidgets.QGridLayout(nombre_place)
        nombre_place.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.horizontalLayout_2.addItem(spacerItem)
        
        self.Clb_place_retour = QtWidgets.QCommandLinkButton(nombre_place)
        self.Clb_place_retour.setObjectName("Clb_place_retour")
        self.Clb_place_retour.setStyleSheet("color: white")
        self.Clb_place_retour.setFont(font)
        
        self.horizontalLayout_2.addWidget(self.Clb_place_retour)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.Tl_tarif = QtWidgets.QLabel(nombre_place)
        self.Tl_tarif.setObjectName("Tl_tarif")
        self.Tl_tarif.setStyleSheet("color: white")
        self.Tl_tarif.setFont(font_titre)
        
        self.verticalLayout.addWidget(self.Tl_tarif)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Tl_nb_places_6ans = QtWidgets.QLabel(nombre_place)
        self.Tl_nb_places_6ans.setObjectName("Tl_nb_places_6ans")
        self.Tl_nb_places_6ans.setStyleSheet("color: white")
        self.Tl_nb_places_6ans.setFont(font)
        
        self.gridLayout.addWidget(self.Tl_nb_places_6ans, 1, 2, 1, 1)
        self.Tl_nb_place_adulte = QtWidgets.QLabel(nombre_place)
        self.Tl_nb_place_adulte.setObjectName("Tl_nb_place_adulte")
        self.Tl_nb_place_adulte.setStyleSheet("color: white")
        self.Tl_nb_place_adulte.setFont(font)
        
        self.gridLayout.addWidget(self.Tl_nb_place_adulte, 0, 2, 1, 1)
        self.Pb_moins_6ans_2 = QtWidgets.QPushButton(nombre_place)
        self.Pb_moins_6ans_2.setObjectName("Pb_moins_6ans_2")
        self.Pb_moins_6ans_2.setStyleSheet("color: white")
        self.Pb_moins_6ans_2.setFont(font)
        
        self.gridLayout.addWidget(self.Pb_moins_6ans_2, 1, 3, 1, 1)
        self.Pb_moins_26ans = QtWidgets.QPushButton(nombre_place)
        self.Pb_moins_26ans.setObjectName("Pb_moins_26ans")
        self.Pb_moins_26ans.setStyleSheet("color: white")
        self.Pb_moins_26ans.setFont(font)
        
        self.gridLayout.addWidget(self.Pb_moins_26ans, 3, 1, 1, 1)
        self.Pb_moins_6ans = QtWidgets.QPushButton(nombre_place)
        self.Pb_moins_6ans.setObjectName("Pb_moins_6ans")
        self.Pb_moins_6ans.setStyleSheet("color: white")
        self.Pb_moins_6ans.setFont(font)
        
        self.gridLayout.addWidget(self.Pb_moins_6ans, 1, 1, 1, 1)
        self.Pb_moins_adulte = QtWidgets.QPushButton(nombre_place)
        self.Pb_moins_adulte.setObjectName("Pb_moins_adulte")
        self.Pb_moins_adulte.setStyleSheet("color: white")
        self.Pb_moins_adulte.setFont(font)
        
        self.gridLayout.addWidget(self.Pb_moins_adulte, 0, 1, 1, 1)
        self.Pb_plus_26ans = QtWidgets.QPushButton(nombre_place)
        self.Pb_plus_26ans.setObjectName("Pb_plus_26ans")
        self.Pb_plus_26ans.setStyleSheet("color: white")
        self.Pb_plus_26ans.setFont(font)
        
        self.gridLayout.addWidget(self.Pb_plus_26ans, 3, 3, 1, 1)
        self.Pb_plus_adulte = QtWidgets.QPushButton(nombre_place)
        self.Pb_plus_adulte.setObjectName("Pb_plus_adulte")
        self.Pb_plus_adulte.setStyleSheet("color: white")
        self.Pb_plus_adulte.setFont(font)
        
        self.gridLayout.addWidget(self.Pb_plus_adulte, 0, 3, 1, 1)
        self.Tl_nb_place_26ans = QtWidgets.QLabel(nombre_place)
        self.Tl_nb_place_26ans.setObjectName("Tl_nb_place_26ans")
        self.Tl_nb_place_26ans.setStyleSheet("color: white")
        self.Tl_nb_place_26ans.setFont(font)
        
        self.gridLayout.addWidget(self.Tl_nb_place_26ans, 3, 2, 1, 1)
        self.Tl_tarif_moins_6ans = QtWidgets.QLabel(nombre_place)
        self.Tl_tarif_moins_6ans.setObjectName("Tl_tarif_moins_6ans")
        self.Tl_tarif_moins_6ans.setStyleSheet("color: white")
        self.Tl_tarif_moins_6ans.setFont(font)
        
        self.gridLayout.addWidget(self.Tl_tarif_moins_6ans, 1, 0, 1, 1)
        self.Tl_tarif_moins_26ans = QtWidgets.QLabel(nombre_place)
        self.Tl_tarif_moins_26ans.setObjectName("Tl_tarif_moins_26ans")
        self.Tl_tarif_moins_26ans.setStyleSheet("color: white")
        self.Tl_tarif_moins_26ans.setFont(font)
        
        self.gridLayout.addWidget(self.Tl_tarif_moins_26ans, 3, 0, 1, 1)
        self.Tl_prix_adulte = QtWidgets.QLabel(nombre_place)
        self.Tl_prix_adulte.setObjectName("Tl_prix_adulte")
        self.Tl_prix_adulte.setStyleSheet("color: white")
        self.Tl_prix_adulte.setFont(font)
        
        self.gridLayout.addWidget(self.Tl_prix_adulte, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.Tl_lunette = QtWidgets.QLabel(nombre_place)
        self.Tl_lunette.setObjectName("Tl_lunette")
        self.Tl_lunette.setStyleSheet("color: white")
        self.Tl_lunette.setFont(font)
        
        self.verticalLayout.addWidget(self.Tl_lunette)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Clb_place_suivant = QtWidgets.QCommandLinkButton(nombre_place)
        self.Clb_place_suivant.setObjectName("Clb_place_suivant")
        self.Clb_place_suivant.setStyleSheet("color: white")
        self.Clb_place_suivant.setFont(font)
        
        self.horizontalLayout.addWidget(self.Clb_place_suivant)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(nombre_place)
        QtCore.QMetaObject.connectSlotsByName(nombre_place)

    def retranslateUi(self, nombre_place):
        _translate = QtCore.QCoreApplication.translate
        nombre_place.setWindowTitle(_translate("nombre_place", "Tarif"))
        self.Clb_place_retour.setText(_translate("nombre_place", "Retour"))
        self.Tl_tarif.setText(_translate("nombre_place", "Veuillez choisir vos tarifs"))
        self.Tl_nb_places_6ans.setText(_translate("nombre_place", "TextLabel"))
        self.Tl_nb_place_adulte.setText(_translate("nombre_place", "TextLabel"))
        self.Pb_moins_6ans_2.setText(_translate("nombre_place", "+"))
        self.Pb_moins_26ans.setText(_translate("nombre_place", "-"))
        self.Pb_moins_6ans.setText(_translate("nombre_place", "-"))
        self.Pb_moins_adulte.setText(_translate("nombre_place", "-"))
        self.Pb_plus_26ans.setText(_translate("nombre_place", "+"))
        self.Pb_plus_adulte.setText(_translate("nombre_place", "+"))
        self.Tl_nb_place_26ans.setText(_translate("nombre_place", "TextLabel"))
        self.Tl_tarif_moins_6ans.setText(_translate("nombre_place", "TextLabel"))
        self.Tl_tarif_moins_26ans.setText(_translate("nombre_place", "TextLabel"))
        self.Tl_prix_adulte.setText(_translate("nombre_place", "TextLabel"))
        self.Tl_lunette.setText(_translate("nombre_place", "Offre spéciale!!! Les lunettes 3D sont offertes"))
        self.Clb_place_suivant.setText(_translate("nombre_place", "Suivant"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    

    nombre_place = QtWidgets.QWidget()
    ui = Ui_nombre_place()
    ui.setupUi(nombre_place)
    nombre_place.show()
    sys.exit(app.exec_())
