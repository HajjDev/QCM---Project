import os

def clear_console():
    """
    pré: void
    post: void
    explication:
    Cette fonction efface la console en fonction du système d'exploitation.
    Si le système est Windows (os.name == 'nt'), elle exécute la commande 'cls' pour nettoyer la console.
    Pour les autres systèmes (Linux, macOS), elle exécute la commande 'clear'.
    """
    # Vérifie si le système d'exploitation est Windows
    if os.name == 'nt':  
        os.system('cls')  # Commande pour effacer la console sur Windows
    else:  
        os.system('clear')  # Commande pour effacer la console sur les systèmes Unix (Linux, macOS)
