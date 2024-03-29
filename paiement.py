# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jcmol\Documents\GitHub\projet-4-cinoche\paiment.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_paiement(object):
    def setupUi(self, paiement):
        paiement.setObjectName("paiement")
        paiement.resize(904, 487)
        
        font_titre= QtGui.QFont()
        font_titre.setFamily("Arial Black")
        font_titre.setPointSize(15)

        font= QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        
        paiement.setBaseSize(QtCore.QSize(0, 100))
        paiement.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout = QtWidgets.QVBoxLayout(paiement)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        
        self.clb_retour = QtWidgets.QCommandLinkButton(paiement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clb_retour.sizePolicy().hasHeightForWidth())
        self.clb_retour.setSizePolicy(sizePolicy)
        self.clb_retour.setToolTipDuration(-2)
        self.clb_retour.setObjectName("clb_retour")
        self.clb_retour.setStyleSheet("color: white")
        self.clb_retour.setFont(font_titre)
        
        self.horizontalLayout.addWidget(self.clb_retour)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tl_code_carte = QtWidgets.QLabel(paiement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tl_code_carte.sizePolicy().hasHeightForWidth())
        self.tl_code_carte.setSizePolicy(sizePolicy)
        self.tl_code_carte.setMinimumSize(QtCore.QSize(300, 110))
        self.tl_code_carte.setObjectName("tl_code_carte")
        self.tl_code_carte.setStyleSheet("color: white")
        self.tl_code_carte.setFont(font)
        
        self.horizontalLayout_2.addWidget(self.tl_code_carte)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        
        self.tl_recapitulatif = QtWidgets.QLabel(paiement)
        self.tl_recapitulatif.setObjectName("tl_recapitulatif")
        self.tl_recapitulatif.setStyleSheet("color: white")
        self.tl_recapitulatif.setFont(font_titre)
        
        self.verticalLayout_2.addWidget(self.tl_recapitulatif)
        self.le_codesecret = QtWidgets.QLineEdit(paiement)
        self.le_codesecret.setObjectName("le_codesecret")
        self.le_codesecret.setStyleSheet("color: white")
        self.le_codesecret.setFont(font)
        
        self.verticalLayout_2.addWidget(self.le_codesecret)
        self.tl_code_secret = QtWidgets.QLabel(paiement)
        self.tl_code_secret.setObjectName("tl_code_secret")
        self.tl_code_secret.setStyleSheet("color: white")
        self.tl_code_secret.setFont(font_titre)
        
        self.verticalLayout_2.addWidget(self.tl_code_secret)
        self.le_code_carte = QtWidgets.QLineEdit(paiement)
        self.le_code_carte.setObjectName("le_code_carte")
        self.le_code_carte.setStyleSheet("color: white")
        self.le_code_carte.setFont(font)
        
        self.verticalLayout_2.addWidget(self.le_code_carte)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.clb_suivant = QtWidgets.QCommandLinkButton(paiement)
        self.clb_suivant.setObjectName("clb_suivant")
        self.clb_suivant.setStyleSheet("color: white")
        self.clb_suivant.setFont(font_titre)
        
        self.horizontalLayout_3.addWidget(self.clb_suivant)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(paiement)
        QtCore.QMetaObject.connectSlotsByName(paiement)

    def retranslateUi(self, paiement):
        _translate = QtCore.QCoreApplication.translate
        paiement.setWindowTitle(_translate("paiement", "Dialog"))
        self.clb_retour.setText(_translate("paiement", "Retour"))
        self.tl_code_carte.setText(_translate("paiement", "TextLabel"))
        self.tl_recapitulatif.setText(_translate("paiement", "Code carte bleu"))
        self.tl_code_secret.setText(_translate("paiement", "Code secret"))
        self.clb_suivant.setText(_translate("paiement", "Suivant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    

    paiement = QtWidgets.QWidget()
    ui = Ui_paiement()
    ui.setupUi(paiement)
    paiement.show()
    sys.exit(app.exec_())
