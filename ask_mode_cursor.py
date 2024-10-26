import curses

def ask_mode_cursor():
    """
    pré: void
    post: mode, char
    explication: 
    Cette fonction permet à l'utilisateur de choisir un mode parmi quatre options ("Normal", 
    "Eliminatoire", "Adaptatif", "Comparatif") en utilisant les touches fléchées et la touche "Entrée".
    Elle utilise la bibliothèque `curses` pour gérer l'interface en ligne de commande.
    Retourne la chaîne de caractères correspondant au mode choisi par l'utilisateur.
    """
    
    modes = [
        "Normal",        # Mode standard
        "Eliminatoire",  # Mode avec élimination
        "Adaptatif",     # Mode qui s'adapte aux réponses
        "Comparatif"     # Mode comparatif
    ]

    # Fonction interne utilisant la bibliothèque curses pour afficher l'interface de sélection
    def select_mode_with_curses(stdscr):
        curses.curs_set(0)  # Masquer le curseur
        stdscr.keypad(True)  # Activer les touches spéciales (comme les flèches directionnelles)
        
        selected_index = 0  # L'index du mode actuellement sélectionné
        answered = False     # Indicateur pour savoir si l'utilisateur a validé sa sélection

        while not answered:
            stdscr.clear()  # Effacer l'écran pour un affichage propre
            
            # Afficher la question en haut
            stdscr.addstr(0, 0, "Quel mode choisissez-vous ?")
            
            # Boucle pour afficher les options de mode
            for index in range(len(modes)):
                if index == selected_index:
                    # Option actuellement sélectionnée (affichage en inversé)
                    stdscr.addstr(index + 1, 0, f"> {index + 1}. {modes[index]}", curses.A_REVERSE)
                else:
                    # Autres options (affichage standard)
                    stdscr.addstr(index + 1, 0, f"  {index + 1}. {modes[index]}")

            # Instruction à l'utilisateur
            stdscr.addstr(len(modes) + 2, 0, "Utilisez les flèches pour naviguer et 'Entrée' pour confirmer.")

            # Capturer l'entrée de l'utilisateur
            key = stdscr.getch()

            # Navigation avec les touches directionnelles
            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(modes)  # Se déplacer vers le haut
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(modes)  # Se déplacer vers le bas
            elif key == curses.KEY_ENTER or key in [10, 13]:  # Touche "Entrée" (validation)
                answered = True  # Confirme la sélection

        # Retourne le mode choisi par l'utilisateur
        return modes[selected_index]  
    
    # Utilisation de curses.wrapper pour exécuter l'application curses proprement
    return curses.wrapper(select_mode_with_curses)
