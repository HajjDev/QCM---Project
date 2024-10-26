from load_qcm import load_qcm
import glob
import curses

def extract_qcms(qcms):
    """
    pré: qcms, list of str
    post: new_qcms, list of str
    explication:
    Cette fonction prend une liste de fichiers de QCM (chemins de fichiers) et extrait uniquement
    les noms de fichiers sans extension ni chemin. Retourne une liste des noms de QCM sous forme de chaînes de caractères.
    """
    new_qcms = []
    for qcm in qcms:
        new_qcms.append(qcm[2:-4])  # Retirer './' au début et '.txt' à la fin
    return new_qcms

def ask_qcm_cursor():
    """
    pré: void
    post: qcm, list
    explication: 
    Cette fonction utilise une interface de sélection pour permettre à l'utilisateur de choisir un fichier QCM 
    dans le répertoire courant. Elle affiche les fichiers trouvés dans une interface en ligne de commande contrôlée 
    par les flèches de direction et la touche "Entrée" via `curses`.
    La fonction continue de redemander un choix si le QCM sélectionné n'a pas pu être chargé.
    Retourne la liste des questions du QCM une fois chargé avec succès.
    """
    
    qcms = glob.glob('./*.txt')  # Liste des fichiers QCM au format .txt dans le répertoire courant
    qcms = extract_qcms(qcms)    # Extrait uniquement les noms des QCM sans extension

    # Fonction interne utilisant la bibliothèque curses pour afficher l'interface de sélection
    def select_qcm_with_curses(stdscr):
        curses.curs_set(0)  # Masquer le curseur
        stdscr.keypad(True)  # Activer les touches spéciales (flèches directionnelles)
        
        selected_index = 0  # Index de l'option actuellement sélectionnée
        answered = False     # Indicateur pour savoir si l'utilisateur a validé sa sélection
        error_message = ""   # Message d'erreur si le chargement échoue

        while not answered:
            stdscr.clear()  # Effacer l'écran pour un affichage propre
            
            # Afficher un message d'erreur si le chargement du QCM a échoué
            if error_message:
                stdscr.addstr(0, 0, error_message)
                error_message = ""
            
            # Afficher la question en haut
            stdscr.addstr(1, 0, "Sélectionnez un QCM à charger:")

            # Boucle pour afficher les options de QCM
            for index in range(len(qcms)):
                if index == selected_index:
                    # Option actuellement sélectionnée (affichage en inversé)
                    stdscr.addstr(index + 2, 0, f"> {index + 1}. {qcms[index]}", curses.A_REVERSE)
                else:
                    # Autres options (affichage standard)
                    stdscr.addstr(index + 2, 0, f"  {index + 1}. {qcms[index]}")

            # Instructions pour l'utilisateur
            stdscr.addstr(len(qcms) + 3, 0, "Utilisez les flèches pour naviguer et 'Entrée' pour confirmer.")

            # Capturer l'entrée de l'utilisateur
            key = stdscr.getch()

            # Navigation avec les touches directionnelles
            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(qcms)  # Se déplacer vers le haut
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(qcms)  # Se déplacer vers le bas
            elif key == curses.KEY_ENTER or key in [10, 13]:  # Touche "Entrée" (validation)
                # Tente de charger le QCM sélectionné
                qcm = load_qcm(qcms[selected_index])
                if qcm is False:
                    error_message = "Le QCM n'a pas pu être chargé. Veuillez en choisir un autre."
                else:
                    return qcm  # Retourne le QCM chargé si le chargement est réussi
    
    # Utilisation de curses.wrapper pour exécuter l'application curses proprement
    return curses.wrapper(select_qcm_with_curses)
