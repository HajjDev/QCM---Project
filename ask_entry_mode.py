from clear_console import clear_console

def ask_entry_mode():
    """
    pré: void
    post: mode, char
    explication: 
    Cette fonction demande à l'utilisateur de choisir un mode d'entrée pour un QCM. 
    L'utilisateur peut choisir entre deux modes : "cursor" (flèches directionnelles) ou "kb" (clavier).
    Elle continue de demander une entrée valide tant qu'une réponse appropriée (1 ou 2) n'a pas été donnée.
    Retourne la chaîne de caractères correspondant au mode choisi par l'utilisateur.
    """
    
    answered = False  # Indicateur pour vérifier si l'utilisateur a fourni une réponse valide
    modes = [
        "cursor",  # Mode utilisant les flèches directionnelles
        "kb"       # Mode utilisant le clavier
    ]
    message = ""  # Message pour afficher les erreurs en cas de saisie incorrecte

    # Boucle tant qu'aucune réponse valide n'est donnée
    while not answered:
        clear_console()  # Efface la console pour un affichage propre
        if len(message) > 0:
            print(message)  # Affiche un message d'erreur si nécessaire
            
        try:
            # Demande à l'utilisateur de choisir un mode via une entrée numérique
            chosen_mode = int(input("""
Choisissez le mode de controle du QCM:
1. Flèches directionnelles
2. Clavier

"""))
            # Si l'utilisateur choisit un des modes valides (1 ou 2), retourne le mode correspondant
            if chosen_mode == 1 or chosen_mode == 2:
                return modes[chosen_mode - 1]
            else:
                # Si la réponse n'est pas valide, un message d'erreur est stocké pour l'afficher à la prochaine itération
                message = 'Choisissez un mode convenable.'
        
        except:
            # En cas d'exception (par exemple si l'utilisateur entre autre chose qu'un nombre), affiche un message d'erreur
            message = 'Choisissez un mode convenable.'
