from PyQt5 import QtCore, QtGui, QtWidgets
from Ercan_Principal import Ui_EcranPrincipal
from Fiche_Film import Ui_Fiche_Film
from Ecran_Choix import Ui_Choix
from Choix_Siege import Ui_ChoixSiege

from dico_films import *


def Appli_cine():
    
    #Construction Menu Principal
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    #Creation fenetre accueil de type EcranPrincipal
    EcranPrincipal = QtWidgets.QMainWindow()
    accueil = Ui_EcranPrincipal()
    accueil.setupUi(EcranPrincipal)

    #Construction fenetre Fiche de type FIche_Film
    Fiche_Film = QtWidgets.QMainWindow()
    Fiche = Ui_Fiche_Film()
    Fiche.setupUi(Fiche_Film)
    
    #Construction fenetre seance de type Choix
    Choix = QtWidgets.QMainWindow()
    seance = Ui_Choix()
    seance.setupUi(Choix)

    #Construction fenetre siege de type ChoixSiège
    ChoixSiege = QtWidgets.QMainWindow()
    siege = Ui_ChoixSiege()
    siege.setupUi(ChoixSiege)


    #Convertir les images pour etre utilisées dans les fenetres
    def pixmap_image(image):
        
        
        #Lieu de stockage des images A CHANGER AVEC LE BON REPERTOIRE en fonction de là ou se trouvent les fichiers 
        repertoire = "C:\\Users\\Elise\\Desktop\\2022 - 2023 année première\\NSI\\projet4_papa\\images\\"
        file = repertoire + image
        
        #Conversion des Affiche en icon pour les boutons et en Pixmap pour la grande affiche
        return QtGui.QPixmap(file)
        
   

    def Film1_click(): #Fonction executer lorsque l'on clique sur le film 1
 
        #Ajout des textes du film 1
        #Conversion des Affiche en icon pour les boutons et en Pixmap pour la grande affiche
        Fiche.Affiche_Film.setScaledContents(True)
        Fiche.Affiche_Film.setPixmap(pixmap_image("AntMan.jpg"))
        Fiche.Affiche_Film.repaint()
         
        #Initialisation de la Fiche_Film     
        Fiche.Text_Synopsis.setText(dico_cine["1"]["synopsis"])
        Fiche.Text_Genre.setText(dico_cine["1"]["genre"])
        Fiche.Text_Genre_2.setText(dico_cine["1"]["acteurs"])
        Fiche.Text_Duree.setText(dico_cine["1"]["duree"])
        Fiche.PB_Seance1.setText("Réserver")
        Fiche.PB_Seance1.clicked.connect(Choix.show)

        #Initialisation de la Choix séances     
        seance.Affiche_FIlm.setPixmap(pixmap_image("AntMan.jpg"))
        seance.Affiche_FIlm.repaint()
        seance.PB_choix1.setText(dico_cine["1"]["Seance1"])
        seance.PB_choix1.clicked.connect(ChoixSiege.show)
        seance.PB_choix2.setText(dico_cine["1"]["Seance2"])
        seance.PB_choix3.setText(dico_cine["1"]["Seance3"])

        #Fonction Initialisation des places disponibles
        def Situation_salle(json_file, salle):
            import json
            
            def open_json(json_file, mode):
                with open(json_file, mode) as f:
                    d_f = json.load(f)
                return d_f

            #Lecture di fichier json
            dico_salle = open_json(json_file, "r")
            
            #Verrouillage des siege occupés
            if dico_salle["1"]["A2"]==1:
                salle.A2.setEnabled(False)
                salle.A2.setChecked(True)
                
        #Application sur les séances
        Situation_salle("C:\\Users\\Elise\\Desktop\\2022 - 2023 année première\\NSI\\projet4_papa\\s_3_10.json", siege)
            
            
            
        

        
        #ouverture Fiche Film
        Fiche_Film.show()


    def Film2_click():

        
       
 
        #Ajout des textes du film 1

        #Conversion des Affiche en icon pour les boutons et en Pixmap pour la grande affiche   
        Fiche.Affiche_Film.setScaledContents(True)
        Fiche.Affiche_Film.setPixmap(pixmap_image("Creed.jpg"))
        Fiche.Affiche_Film.repaint()
        
      
        Fiche.Text_Synopsis.setText(dico_cine["2"]["synopsis"])
        Fiche.Text_Genre.setText(dico_cine["2"]["genre"])
        Fiche.Text_Genre_2.setText(dico_cine["2"]["acteurs"])
        Fiche.Text_Duree.setText(dico_cine["2"]["duree"])

        Fiche.PB_Seance1.setText("Réserver")
        Fiche.PB_Seance1.clicked.connect(Choix.show)

        #Initialisation de la Choix séances     
        seance.Affiche_FIlm.setPixmap(pixmap_image("Creed.jpg"))
        seance.Affiche_FIlm.repaint()
        seance.PB_choix1.setText(dico_cine["2"]["Seance1"])
        seance.PB_choix2.setText(dico_cine["2"]["Seance2"])
        seance.PB_choix3.setText(dico_cine["2"]["Seance3"])

        #ouverture Fiche Film
        Fiche_Film.show()            

    def Film3_click():

        
       
 
        #Ajout des textes du film 1


         #Conversion des Affiche en icon pour les boutons et en Pixmap pour la grande affiche
        Fiche.Affiche_Film.setScaledContents(True)
        Fiche.Affiche_Film.setPixmap(pixmap_image("Seoul.jpg"))
        Fiche.Affiche_Film.repaint()
 
        Fiche.Text_Synopsis.setText(dico_cine["3"]["synopsis"])
        Fiche.Text_Genre.setText(dico_cine["3"]["genre"])
        Fiche.Text_Genre_2.setText(dico_cine["3"]["acteurs"])
        Fiche.Text_Duree.setText(dico_cine["3"]["duree"])

        Fiche.PB_Seance1.setText("Réserver")
        Fiche.PB_Seance1.clicked.connect(Choix.show)

        #Initialisation de la Choix séances     
        seance.Affiche_FIlm.setPixmap(pixmap_image("Seoul.jpg"))
        seance.Affiche_FIlm.repaint()
        seance.PB_choix1.setText(dico_cine["3"]["Seance1"])
        seance.PB_choix2.setText(dico_cine["3"]["Seance2"])
        seance.PB_choix3.setText(dico_cine["3"]["Seance3"])

        
        #ouverture Fiche Film
        Fiche_Film.show()

    def Film4_click():

        
        
 
        #Ajout des textes du film 1


        #Conversion des Affiche en icon pour les boutons et en Pixmap pour la grande affiche       
        Fiche.Affiche_Film.setScaledContents(True)
        Fiche.Affiche_Film.setPixmap(pixmap_image("Galaxie.jpg"))
        Fiche.Affiche_Film.repaint()
        
        Fiche.Text_Synopsis.setText(dico_cine["4"]["synopsis"])
        Fiche.Text_Genre.setText(dico_cine["4"]["genre"])
        Fiche.Text_Genre_2.setText(dico_cine["4"]["acteurs"])
        Fiche.Text_Duree.setText(dico_cine["4"]["duree"])

        Fiche.PB_Seance1.setText("Réserver")
        Fiche.PB_Seance1.clicked.connect(Choix.show)

        #Initialisation de la Choix séances     
        seance.Affiche_FIlm.setPixmap(pixmap_image("Galaxie.jpg"))
        seance.Affiche_FIlm.repaint()
        seance.PB_choix1.setText(dico_cine["4"]["Seance1"])
        seance.PB_choix2.setText(dico_cine["4"]["Seance2"])
        seance.PB_choix3.setText(dico_cine["4"]["Seance3"])

        
        #ouverture Fiche Film
        Fiche_Film.show()

        
    def Film5_click():

        
       
 
        #Ajout des textes du film 1


        #Conversion des Affiche en icon pour les boutons et en Pixmap pour la grande affiche
        Fiche.Affiche_Film.setScaledContents(True)
        Fiche.Affiche_Film.setPixmap(pixmap_image("Elemental.jpg"))
        Fiche.Affiche_Film.repaint()
        
      
        Fiche.Text_Synopsis.setText(dico_cine["5"]["synopsis"])
        Fiche.Text_Genre.setText(dico_cine["5"]["genre"])
        Fiche.Text_Genre_2.setText(dico_cine["5"]["acteurs"])
        Fiche.Text_Duree.setText(dico_cine["5"]["duree"])

        Fiche.PB_Seance1.setText("Réserver")
        Fiche.PB_Seance1.clicked.connect(Choix.show)

        #Initialisation de la Choix séances     
        seance.Affiche_FIlm.setPixmap(pixmap_image("Elemental.jpg"))
        seance.Affiche_FIlm.repaint()
        seance.PB_choix1.setText(dico_cine["5"]["Seance1"])
        seance.PB_choix2.setText(dico_cine["5"]["Seance2"])
        seance.PB_choix3.setText(dico_cine["5"]["Seance3"])
        
        #ouverture Fiche Film
        Fiche_Film.show()

    accueil.PB_Film1.clicked.connect(Film1_click)
    accueil.PB_Film1_2.clicked.connect(Film2_click)
    accueil.PB_Film1_3.clicked.connect(Film3_click)
    accueil.PB_Film1_4.clicked.connect(Film4_click)
    accueil.PB_Film1_5.clicked.connect(Film5_click)

    EcranPrincipal.show()
    sys.exit(app.exec_())    



Appli_cine()
