from PyQt5 import QtWidgets

from nombre_place_new import Ui_nombre_place
from Choix_Siege import Ui_ChoixSiege
from paiement import Ui_paiement

tarif1=10
tarif2="gratuit"
tarif3=5
#enlever quand rattaché 
siege_selectionne=5

def appli(tarif3,tarif1,tarif2,siege_selectionne):
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

    #Construction fenetre paiement
    paiement = QtWidgets.QWidget()
    payer=  Ui_paiement()
    payer.setupUi(paiement)
    
    
    #initialisation des tarif si on veut changer de sujet
    place.Tl_tarif_moins_26ans.setText("moins de 26 ans: "+str (tarif3)+" €")
    place.Tl_prix_adulte.setText("Adulte:"+str (tarif1)+" €")
    place.Tl_tarif_moins_6ans.setText("Moins de 6 ans: "+ tarif2)
    place.Tl_nb_places_6ans.setText("0")
    place.Tl_nb_place_26ans.setText("0")
    place.Tl_nb_place_adulte.setText("0")
    place.Tl_lunette.setText("Vous devez encore selectionnez: "+ str(siege_selectionne)+"place(s)\n Offre spéciale!!! Les lunettes 3D sont offertes")
    

    
    
    # action bouton retour à la page précédente
    def place_retour():
        nombre_place.hide()
        ChoixSiege.show()
    # action bouton pour ajouter des places moins de 6 ans
    def ajout_place_6ans():
        if int(place.Tl_nb_place_adulte.text())+int(place.Tl_nb_places_6ans.text())+int(place.Tl_nb_place_26ans.text())==siege_selectionne:
            place.Pb_moins_6ans_2.setEnabled(False)
        else:
            place_6ans=int(place.Tl_nb_places_6ans.text())+1
            place.Tl_nb_places_6ans.setText(str(place_6ans))
            place.Pb_moins_6ans_2.setEnabled(True)
            place.Pb_moins_6ans.setEnabled(True)
            place.Tl_lunette.setText("Vous devez encore selectionnez: "+ str(siege_selectionne-int(place.Tl_nb_place_adulte.text())-int(place.Tl_nb_places_6ans.text())-int(place.Tl_nb_place_26ans.text()))+"place(s)\n Offre spéciale!!! Les lunettes 3D sont offertes")
    #action bouton pour retirer des places moins de 6 ans
    def retirer_place_6ans():
        if int(place.Tl_nb_places_6ans.text())==0:
            place.Pb_moins_6ans.setEnabled(False)
        else:
            place_6ans=int(place.Tl_nb_places_6ans.text())-1
            place.Tl_nb_places_6ans.setText(str(place_6ans))
            place.Pb_moins_6ans.setEnabled(True)
            place.Pb_moins_6ans_2.setEnabled(True)
            place.Tl_lunette.setText("Vous devez encore selectionnez: "+ str(siege_selectionne-int(place.Tl_nb_place_adulte.text())-int(place.Tl_nb_places_6ans.text())-int(place.Tl_nb_place_26ans.text()))+"place(s)\n Offre spéciale!!! Les lunettes 3D sont offertes")
    #action bouton pour ajouter des places moins de 26 ans
    def ajout_place_26ans():
        if int(place.Tl_nb_place_adulte.text())+int(place.Tl_nb_places_6ans.text())+int(place.Tl_nb_place_26ans.text())==siege_selectionne:
            place.Pb_plus_26ans.setEnabled(False)
        else:
            place_26ans=int(place.Tl_nb_place_26ans.text())+1
            place.Tl_nb_place_26ans.setText(str(place_26ans))
            place.Pb_plus_26ans.setEnabled(True)
            place.Pb_moins_26ans.setEnabled(True)
            place.Tl_lunette.setText("Vous devez encore selectionnez: "+ str(siege_selectionne-int(place.Tl_nb_place_adulte.text())-int(place.Tl_nb_places_6ans.text())-int(place.Tl_nb_place_26ans.text()))+"place(s)\n Offre spéciale!!! Les lunettes 3D sont offertes")
    #action bouton pour retirer des places moins de 6 ans
    def retirer_place_26ans():
        if int(place.Tl_nb_place_26ans.text())==0:
            place.Pb_moins_26ans.setEnabled(False)
        else:
            place_26ans=int(place.Tl_nb_place_26ans.text())-1
            place.Tl_nb_place_26ans.setText(str(place_26ans))
            place.Pb_moins_26ans.setEnabled(True)
            place.Pb_plus_26ans.setEnabled(True)
            place.Tl_lunette.setText("Vous devez encore selectionnez: "+ str(siege_selectionne-int(place.Tl_nb_place_adulte.text())-int(place.Tl_nb_places_6ans.text())-int(place.Tl_nb_place_26ans.text()))+"place(s)\n Offre spéciale!!! Les lunettes 3D sont offertes")
        
    #action bouton pour ajouter des places adultes
    def ajout_place_adulte():
        if int(place.Tl_nb_place_adulte.text())+int(place.Tl_nb_places_6ans.text())+int(place.Tl_nb_place_26ans.text())==siege_selectionne:
            place.Pb_plus_adulte.setEnabled(False)
        else:
            place_adulte=int(place.Tl_nb_place_adulte.text())+1
            place.Tl_nb_place_adulte.setText(str(place_adulte))
            place.Pb_plus_adulte.setEnabled(True)
            place.Pb_moins_adulte.setEnabled(True)
            place.Tl_lunette.setText("Vous devez encore selectionnez: "+ str(siege_selectionne-int(place.Tl_nb_place_adulte.text())-int(place.Tl_nb_places_6ans.text())-int(place.Tl_nb_place_26ans.text()))+"place(s)\n Offre spéciale!!! Les lunettes 3D sont offertes")
    #action bouton pour retirer des places adultes
    
    def retirer_place_adulte():
        
        if int(place.Tl_nb_place_adulte.text())==0:
            place.Pb_moins_adulte.setEnabled(False)
        else:
            place_adulte=int(place.Tl_nb_place_adulte.text())-1
            place.Tl_nb_place_adulte.setText(str(place_adulte))
            place.Pb_moins_adulte.setEnabled(True)
            place.Pb_plus_adulte.setEnabled(True)
            place.Tl_lunette.setText("Vous devez encore selectionnez: "+ str(siege_selectionne-int(place.Tl_nb_place_adulte.text())-int(place.Tl_nb_places_6ans.text())-int(place.Tl_nb_place_26ans.text()))+"place(s)\n Offre spéciale!!! Les lunettes 3D sont offertes")
            return 
    #action bouton page suivante
    def place_suivant():
        if int(place.Tl_nb_place_adulte.text())+int(place.Tl_nb_places_6ans.text())+int(place.Tl_nb_place_26ans.text())==siege_selectionne:
            nb_adulte=int(place.Tl_nb_place_adulte.text())
            nb_6ans=int(place.Tl_nb_places_6ans.text())
            nb_26ans=int(place.Tl_nb_place_26ans.text())
            nombre_place.hide()
            paiement.show()
            payer.tl_code_carte.setText("Récapitulatif \n"
                                        +str(place.Tl_nb_places_6ans.text())+" place(s) moins de 6 ans soit "+str(tarif2)+"\n"
                                        +str(place.Tl_nb_place_26ans.text())+" place(s) moins de 26 ans soit " +str(tarif3*int(place.Tl_nb_place_26ans.text()))+ " € \n"
                                        + str(place.Tl_nb_place_adulte.text())+ "place(s) adulte"+str(tarif1*int(place.Tl_nb_place_adulte.text()))+" € \n"
                                        +"       Total= "+ str(int(place.Tl_nb_place_adulte.text())*tarif1+int(place.Tl_nb_place_26ans.text())*tarif3)+" €")
                                                                                                                   
                                        
            
        

    #bouton de fenetre tarif 
    place.Clb_place_retour.clicked.connect(place_retour)
    place.Pb_moins_6ans_2.clicked.connect(ajout_place_6ans)
    place.Pb_moins_6ans.clicked.connect(retirer_place_6ans)
    place.Pb_plus_26ans.clicked.connect(ajout_place_26ans)
    place.Pb_moins_26ans.clicked.connect(retirer_place_26ans)
    place.Pb_plus_adulte.clicked.connect(ajout_place_adulte)
    place.Pb_moins_adulte.clicked.connect(retirer_place_adulte)
    place.Clb_place_suivant.clicked.connect(place_suivant)
#fenetre paiement
    
    
        
    #payer.tl_code_carte.setText()
                                
    def payer_retour():
        paiement.hide()
        nombre_place.show()
    def payer_suivant():
        if len(list(payer.le_codesecret.text()))==16 and len(list(payer.le_code_carte.text()))==3 and payer.le_codesecret.inputMask()==9999:
            paiement.hide()
            nombre_place.show()
            

    #bouton de fenetre paiement
    payer.clb_retour.clicked.connect(payer_retour)
    payer.le_code_carte.setEchoMode(2)
    
    payer.clb_suivant.clicked.connect(payer_suivant)
    
    nombre_place.show()
    sys.exit(app.exec_())
    
appli(tarif3,tarif1,tarif2,siege_selectionne)
