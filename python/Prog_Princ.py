from PyQt5 import QtCore ,QtGui ,QtWidgets
from Ercan_Principal import Ui_EcranPrincipal
from Fiche_Film import Ui_Fiche_Film


def Appli_cine():
    
    #Construction Menu Principal
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    EcranPrincipal = QtWidgets.QMainWindow()
    accueil = Ui_EcranPrincipal()
    accueil.setupUi(EcranPrincipal)

    #Construction Fiche Film
    Fiche_Film = QtWidgets.QMainWindow()
    ui = Ui_Fiche_Film()
    ui.setupUi(Fiche_Film)
   

    def Film1_click():
        
        EcranPrincipal.hide()

       
        
        Fiche_Film.show()
        

    accueil.PB_Film1.clicked.connect(Film1_click)


    def ReturnButton_click():
        Fiche_film.hide()

        
        EcranPrincipal.show()

    ui.ReturnButton.clicked.connect(ReturnButton_click)


    
    EcranPrincipal.show()
    sys.exit(app.exec_())


Appli_cine()
