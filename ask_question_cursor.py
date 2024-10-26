import curses
import random

def contain_similar_elements(arr):
    """
    pré: arr, list
    post: bool
    explication:
    Cette fonction vérifie si un tableau contient des éléments similaires.
    Elle retourne True si des éléments similaires sont trouvés, sinon False.
    """
    return len(set(arr)) != len(arr)

def true_index(val, arr):
    """
    pré: val, any; arr, list
    post: index, int
    explication:
    Cette fonction retourne l'index original de 'val' dans le tableau 'arr'.
    Si la valeur est trouvée, retourne l'index, sinon None.
    """
    for index in range(len(arr)):
        if arr[index] == val:
            return index

def ask_question_cursor(question, answers):
    """
    pré: question, str; answers, list of str
    post: selected_answers, list of int
    explication:
    Cette fonction affiche une question et un ensemble de réponses sous forme d'une interface utilisant les flèches pour naviguer.
    L'utilisateur peut sélectionner/désélectionner plusieurs réponses avec la touche 'Entrée' et confirmer ses choix.
    Elle retourne les indices originaux des réponses sélectionnées dans la liste 'answers'.
    """
    
    def ask_with_curses(stdscr):
        curses.curs_set(0)  # Masquer le curseur
        stdscr.keypad(True)  # Activer les touches spéciales (flèches directionnelles)
        
        # Mélanger les réponses pour les afficher dans un ordre aléatoire
        shuffled_answers = random.sample(answers, len(answers))
        selected_indices = []  # Indices des réponses sélectionnées
        selected_index = 0  # Indice de la réponse actuellement surlignée
        answered = False  # Indicateur de fin de sélection
        message2show = ""  # Message à afficher en cas d'erreur (ex: aucune sélection faite)

        # Boucle principale de l'interface
        while not answered:
            stdscr.clear()  # Efface l'écran à chaque itération

            if message2show:
                stdscr.addstr(0, 0, message2show)  # Affiche un message d'erreur s'il y en a un
                message2show = ""

            # Afficher la question et une ligne de séparation
            stdscr.addstr(0, 0, question)
            stdscr.addstr(1, 0, "-" * (len(question) + 1))

            # Boucle pour afficher les réponses avec les sélections
            for index in range(len(shuffled_answers)):
                if index == selected_index:
                    # Réponse actuellement surlignée
                    stdscr.addstr(index + 2, 0, f"> {index + 1}. {shuffled_answers[index]}", curses.A_REVERSE)
                elif index in selected_indices:
                    # Réponse sélectionnée avec un "✔"
                    stdscr.addstr(index + 2, 0, f"✔ {index + 1}. {shuffled_answers[index]}", curses.A_REVERSE)
                else:
                    # Réponse non sélectionnée
                    stdscr.addstr(index + 2, 0, f"  {index + 1}. {shuffled_answers[index]}")

            # Ajouter une option "Confirmer" à la fin
            confirm_option_index = len(shuffled_answers)
            if selected_index == confirm_option_index:
                stdscr.addstr(confirm_option_index + 3, 0, "> Confirmer", curses.A_REVERSE)
            else:
                stdscr.addstr(confirm_option_index + 3, 0, "  Confirmer")

            # Instructions à l'utilisateur
            stdscr.addstr(confirm_option_index + 5, 0, "Utilisez les flèches pour naviguer, 'Entrée' pour sélectionner/désélectionner et confirmer.")

            # Capture de la touche pressée par l'utilisateur
            key = stdscr.getch()

            # Navigation avec les flèches
            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % (len(shuffled_answers) + 1)
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % (len(shuffled_answers) + 1)
            elif key == curses.KEY_ENTER or key in [10, 13]:  # Touche "Entrée"
                if selected_index == confirm_option_index:  # Si l'utilisateur est sur "Confirmer"
                    if not selected_indices:  # Si aucune réponse n'a été sélectionnée
                        message2show = "Veuillez sélectionner au moins une réponse avant de confirmer."
                    else:
                        answered = True  # Terminer la sélection
                else:
                    # Ajouter ou retirer une réponse de la sélection
                    if selected_index in selected_indices:
                        selected_indices.remove(selected_index)
                    else:
                        selected_indices.append(selected_index)

        # Retourner les indices originaux des réponses sélectionnées
        selected_answers = [true_index(shuffled_answers[i], answers) for i in selected_indices]
        return selected_answers

    return curses.wrapper(ask_with_curses)
