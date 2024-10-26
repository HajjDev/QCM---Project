from clear_console import clear_console

def ask_mode_kb():
    """
    pré: void
    post: mode, char
    explication: 
    Cette fonction permet à l'utilisateur de choisir un mode parmi quatre options 
    ("Normal", "Eliminatoire", "Adaptif", "Comparatif") en entrant le numéro correspondant via le clavier.
    Elle gère les entrées incorrectes (par exemple, texte non numérique ou choix hors des limites).
    Retourne la chaîne de caractères correspondant au mode choisi par l'utilisateur.
    """
    
    answered = False  # Indicateur pour vérifier si l'utilisateur a fourni une réponse valide
    message2show = ""  # Message à afficher en cas d'erreur d'entrée
    modes = [
        "Normal",        # Mode standard
        "Eliminatoire",  # Mode avec élimination
        "Adaptif",       # Mode adaptatif
        "Comparatif"     # Mode comparatif
    ]
  
    # Boucle pour demander à l'utilisateur de choisir un mode jusqu'à ce qu'une réponse valide soit donnée
    while not answered:
        clear_console()  # Efface la console pour un affichage propre
        
        # Affiche un message d'erreur si une entrée incorrecte a été faite précédemment
        if message2show:
            print(message2show)

        # Affiche la liste des modes disponibles
        print("Quel mode choisissez-vous ?")
        for index in range(len(modes)):
            print(str(index+1) + ". " + modes[index])

        print("\n")
        # Demande à l'utilisateur de choisir un mode en entrant un numéro
        answer = input("Choisissez votre mode (le numéro): \n")

        try:
            # Convertit l'entrée utilisateur en un index de la liste des modes
            answerIndex = int(answer) - 1
            # Vérifie si l'index est valide (entre 0 et len(modes) - 1)
            if answerIndex < 0 or answerIndex > len(modes) - 1:
                message2show = "Veuillez entrer un numéro correct"
            else:
                answered = True  # L'utilisateur a donné une réponse valide
        except ValueError:
            # En cas d'entrée non numérique, affiche un message d'erreur
            message2show = "Ce n'est pas un chiffre. Veuillez entrer le numéro du mode"
    
    clear_console()  # Efface la console après validation
    return modes[answerIndex]  # Retourne le mode choisi
