def ajoutJoueur1():
    nom_du_joueur = input("Donne moi ton nom ? : ")
    score1 = open("Iatendry/score.txt", "w")
    score1.write("score de " + nom_du_joueur + "\n")
    score1.close()


# ajoutJoueur1() --> En utilisant cette fonction, on peut ajouter un UNIQUE joueur dans le fichier score.txt,
# la donnée précédente sera écrasée par la nouvelle donnée

def ajoutJoueur2():
    nom_du_joueur = input("Donne moi ton nom ? : ")
    score2 = open("Iatendry/score.txt", "a")
    score2.write("score de " + nom_du_joueur + "\n")
    score2.close()

#ajoutJoueur2() # --> En utilisant cette fonction, on peut ajouter PLUSIEURS joueurs dans le fichier score.txt
# la donnée précédente ne sera pas écrasée par la nouvelle donnée car elle utilise le mode "a" pour append et en français veut dire "ajouter"


def ajoutJoueur3() :
    score3 = open("Iatendry/score.txt", "r")
    for ligne in score3:
        print(ligne)
    score3.close()
    
#ajoutJoueur3() # --> En utilisant cette fonction, on peut afficher le contenu avec un saut de ligne(\n) du fichier score.txt



def nomJoueur() :
    return input("Donne moi ton nom ? : ")

def ajoutScore():
    return input("Donne moi ton score ? : ")


def GameBowling() :
    nom_du_joueur = nomJoueur()
    score = ajoutScore()
    filePath = "Iatendry/scoreBowling.txt"
    score_file = open(filePath, "r")
    # On initialise les différentes variables
    score_moyen = 0
    TEXT_SCORE = "Score de "
    TEXT_SCORE_MOYEN = ", score moyen : "
    TEXT_PARTIE_JOUE = "et nombre de partie jouee : "
    nbPartie = 0
    checkJoueur = False # --> On initialise la variable checkJoueur à False qui regarde si un joueur est présent dans le fichier score.txt
    # On recherche si le joueur est déjà existant dans le fichier score.txt
    countLine = -1 # --> On initialise la variable countLine à -1 pour ne pas compter la première ligne du fichier score.txt
    newlign = ""
    
    
    # On parcourt le fichier score.txt
    for ligne in score_file:
        countLine += 1
        if nom_du_joueur in ligne:
            nbPartie = int((ligne.split("et")[1].split(": ")[1])) + 1
            score_moyen = (float((ligne.split(",")[1].split(": ")[1].split("et")[0])) + int(score)) / nbPartie
            newlign = ligne.replace(ligne, TEXT_SCORE + nom_du_joueur + " : " + str(score) + TEXT_SCORE_MOYEN + str(score_moyen) + " " +  TEXT_PARTIE_JOUE + str(nbPartie) + "\n")
            checkJoueur = True
            
    # On vérifie si le joueur est déjà existant dans le fichier score.txt
    if checkJoueur == False:
        nbPartie = 1
        score_file = open(filePath, "a")
        score_file.write(TEXT_SCORE + nom_du_joueur + " : " + str(score) + TEXT_SCORE_MOYEN + str(score) + " " + TEXT_PARTIE_JOUE + str(nbPartie) + "\n") # --> Si le joueur n'est pas présent dans le fichier score.txt, on l'ajoute avec un score moyen qui est égal à son score initial
    else :
        # On remplace la ligne du joueur par la nouvelle ligne
        with open(filePath, 'r', encoding='utf-8') as file:
            lign = file.readlines()
        lign[countLine] = newlign
        with open(filePath, 'w', encoding='utf-8') as file:
            file.writelines(lign)
            
    #Idéal pour l'affichage d'information
    if (score_moyen == 0) :
        score_moyen = score
    print("Score de " + nom_du_joueur + " : " + score + ", son score moyen : " + str(score_moyen), "et nombre de partie jouee : " + str(nbPartie))
    print("Merci d'avoir joué !")
    score_file.close()
    
            
GameBowling()