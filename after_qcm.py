from clear_console import clear_console

def after_qcm():
    """
    pré: void
    post: bool
    explication:
    Cette fonction demande à l'utilisateur s'il souhaite refaire un autre QCM.
    Elle boucle jusqu'à ce qu'une réponse valide soit fournie :
    - 1 pour "Oui", qui retourne True
    - 2 pour "Non", qui retourne False
    En cas d'entrée non valide (chiffre hors limite ou non numérique), un message d'erreur est affiché.
    """
    done = False  # Indicateur pour savoir si une réponse valide a été obtenue

    try:
        while not done:
            # Demande à l'utilisateur s'il veut refaire un autre QCM
            ask = int(input("""
Voulez-vous refaire un autre QCM?
1 - Oui
2 - Non
"""))

            # Vérifie que la réponse est soit 1 soit 2
            if ask > 2 or ask < 1:
                print("Choisissez une réponse convenable.")  # Affiche un message si la réponse est hors limites
            else:
                done = True  # Réponse valide, on termine la boucle

    except ValueError:
        print("Choisissez une réponse convenable.")  # Affiche un message si l'entrée n'est pas un nombre

    return ask == 1  # Retourne True si l'utilisateur a choisi "Oui", sinon False
