from PyQt5 import QtWidgets

from nombre_place_new import Ui_nombre_place
from Choix_Siege import Ui_ChoixSiege

tarif1="10€"
tarif2="gratuit"
tarif3="5€"
place_adulte=0
#place_6ans= 5
place_26ans=0
def appli(tarif3,tarif1,tarif2):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #Construction de la page nombre_place
    nombre_place = QtWidgets.QWidget()
    place =  Ui_nombre_place()
    place.setupUi(nombre_place)

    #Construction fenetre siege de type ChoixSiège
    ChoixSiege = QtWidgets.QMainWindow()
    siege = Ui_ChoixSiege()
    siege.setupUi(ChoixSiege)
    place_6ans=0
    a=1
    #initialisation des tarif si on veut changer de sujet
    place.Tl_tarif_moins_26ans.setText("moins de 26 ans: "+tarif3)
    place.Tl_prix_adulte.setText("Adulte:"+tarif1)
    place.Tl_tarif_moins_6ans.setText("Moins de 6 ans: "+ tarif2)
    place.Tl_nb_places_6ans.setText(str(place_6ans))

    

    def place_retour():
        nombre_place.hide()
        ChoixSiege.show()
        
    def place_suivant(place_6ans):
        place_6ans=int(place_6ans)+2
        place.Tl_nb_places_6ans.setText(str(place_6ans))
        print (place_6ans)
        #nombre_placehide()
        #paiement.show()
        return int(place_6ans)

    

    place.Clb_place_retour.clicked.connect(place_retour)
    place.Clb_place_suivant.clicked.connect(place_suivant)
   # placde.
    
    nombre_place.show()
    sys.exit(app.exec_())
    

    

appli(tarif3,tarif1,tarif2)
