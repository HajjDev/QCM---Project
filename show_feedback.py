from clear_console import clear_console
from extract_questions import extract_qcm

def show_feedback(questions, answered):
    """
    pré: questions, list of tuples; answered, list of list of int
    post: void
    explication:
    Cette fonction affiche un récapitulatif des réponses données par l'utilisateur pour chaque question. 
    Elle indique pour chaque question si la réponse choisie est correcte (en vert avec une coche) ou incorrecte (en rouge avec une croix).
    La réponse sélectionnée par l'utilisateur est surlignée en blanc pour plus de visibilité.
    Utilise des codes de couleur ANSI pour améliorer l'affichage en console.
    """
    
    # Codes ANSI pour la couleur du texte et de l'arrière-plan
    BLUE = "\033[34m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    TEXT_BLACK = "\033[30m"
    HIGHLIGHT_WHITE = "\033[47m"
    RESET = "\033[0m"

    clear_console()  # Efface la console avant d'afficher le feedback
    print(f"""
Vous avez fini de répondre aux {BLUE}questions{RESET} !
Voici le récapitulatif des questions et des réponses avec votre note :

(La réponse que vous avez choisie est surlignée en blanc.)
    """)

    # Boucle pour afficher chaque question et ses réponses
    for index in range(len(questions)):
        formatted = extract_qcm(questions[index])
        q_title = formatted[0]  # Texte de la question
        q_answers = formatted[1]  # Liste des réponses possibles

        print("\n")
        print(index + 1, ".", q_title)  # Affiche le numéro et le texte de la question
        
        # Affiche chaque réponse pour la question actuelle
        for ans_index in range(len(q_answers)):
            is_correct = questions[index][1][ans_index][1]  # Indicateur si la réponse est correcte
            feedback = questions[index][1][ans_index][2]  # Texte de feedback pour cette réponse
            choosen_by_user = ans_index in answered[index]  # Vérifie si l'utilisateur a choisi cette réponse
            
            # Définition de la couleur d'affichage pour la réponse sélectionnée
            begin = ""
            if choosen_by_user:
                begin = HIGHLIGHT_WHITE + TEXT_BLACK
            
            # Définition de l'affichage de la correction (coche verte ou croix rouge)
            end = ""
            if is_correct:
                end = GREEN + " ✅" + RESET
            else:
                end = RED + " ❌" + RESET
            
            # Affiche la réponse avec surlignage et feedback
            print(begin + "• " + q_answers[ans_index] + RESET + " " + end)
