import time

def estPremier(n):
    if n>1 :
        x = True
        for i in range(2, n):
            if n%i == 0:
                x = False
                break
        if x : return True
    return False


def testEstPremier() :
    try:
        assert estPremier(1) ==  False
        assert estPremier(2) ==  True
        assert estPremier(11) ==  True
        assert estPremier(17) ==  True
        assert estPremier(21) ==  False
        print("estPremier : OK")
    except:
        print("estPremier : ERREUR")
        
        

def nomJoueur() :
    return input("Donne moi ton nom ? : ")


def GameSave(nom_du_joueur,score) :
    filePath = "Iatendry/scoreMultiplication.txt"
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
    print("Score de " + nom_du_joueur + " : " + str(score) + ", son score moyen : " + str(score_moyen), "et nombre de partie jouee : " + str(nbPartie))
    score_file.close()
    
    
       

def InitGameMultplication() :
    nom_joueur = nomJoueur()
    print("Choix des classes CE1 = 1, CE2 = 2, CM1 et supérieur = 3")
    classe = int(input("Donne moi votre classe ?(1,2,3) : "))
    while classe < 1 and classe > 3 :
        print("Votre numéro de classe n'est pas valide")
        classe = int(input("Donne moi votre classe ?(1,2,3) : "))
        
        
    if (classe == 1) :
        print("Vous êtes dans la classe CE1")
        print("Choix des tables de multiplication : 1, 2, 3, 4, 5")
        table = int(input("Donne moi la table ?(1,2,3,4,5) : "))
        while(table < 1 or table > 5) :
            print("La table choisie n'est pas dans la classe CE1")
            table = int(input("Donne moi la table ?(1,2,3,4,5) : "))
            
    if (classe == 2) :
        print("Vous êtes dans la classe CE2")
        print("Choix des tables de multiplication : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
        table = int(input("Donne moi la table ?(1,2,3,4,5,6,7,8,9,10) : "))
        while(table < 1 or table > 10) :
            print("La table choisie n'est pas dans la classe CE2")
            table = int(input("Donne moi la table ?(1,2,3,4,5,6,7,8,9,10) : "))
            
    if (classe == 3) :
        print("Vous êtes dans la classe CM1 et supérieur")
        table = int(input("Donne moi la table ? : "))
    
    
    print("Vous avez choisi la table de multiplication de " + str(table))
    return classe,table,nom_joueur

def Tips() :
    print("--------------------- AIDE ---------------------")
    print("La multiplication est une opération mathématique qui consiste à multiplier un nombre par un autre.")
    print("Pour multiplier deux nombres, on les écrit l'un à côté de l'autre, puis on les multiplie chiffre par chiffre, en commençant par le chiffre des unités.")
    print("Exemple : 3 x 4 = 12")
    print("Vous aurez 10 questions et aurez le droit à une 2nd chance si vous vous trompez")
    print("--------------------- AIDE ---------------------")


    
def GameMultiplication() :
    print("Bienvenue dans le jeu de multiplication")
    classe,table,nom_joueur = InitGameMultplication()
    print("Nous allons commencer le jeu")
    aide = input("Souhaitez vous une explication ?(oui/non) : ")
    if (aide == "oui") :
        Tips()
    
    print("Nous allons vous poser 10 questions")
    
    i = 0
    score = 0
    averageTime = 0
    while(i < 10) :
        print("--------------------- QUESTION " + str(i+1) + " ---------------------")
        print(str(table) + " x " + str(i+1) + " = ?")
        start = time.time()
        reponse = int(input("Votre réponse : "))
        if (reponse == table*(i+1)) :
            score += 1
            print("Bonne réponse")
        else :
            print("Mauvaise réponse")
            print("2nd chance")
            reponse = int(input("Votre réponse : "))
            if (reponse == table*(i+1)) :
                print("Bonne réponse")
                score += 1
            else :
                print("Mauvaise réponse")
                score -= 1
                print("La bonne réponse était : " + str(table*(i+1)))
        end = time.time()
        timeQuestion = end - start
        averageTime += timeQuestion
        i = i + 1
    if (score < 0) :
        score = 0
    print("Votre score est de " + str(score) + "/10")
    print("Votre temps moyen par question est de " + str(round(averageTime/10,3)) + " secondes")
    save = input("Souhaitez vous sauvegarder votre score ?(oui/non) : ")
    if (save == "oui") :
        GameSave(nom_joueur,score)
    if (score > 9) :
        restart = input("Souhaitez vous rejouer ?(oui/non) : ")
    else : 
        restart = "oui"
        print("Votre score est inférieur à 90%, vous devez rejouer")
    
    if (restart == "oui") :
        GameMultiplication()
    print("Merci d'avoir joué")
    


GameMultiplication()
    