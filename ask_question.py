from ask_question_cursor import ask_question_cursor
from ask_question_kb import ask_question_kb

def ask_question(entry, question, answers):
    """
    pré: entry, char; question, str; answers, list of str
    post: selected_indices, list of int
    explication:
    Cette fonction détermine quel mode de saisie utiliser pour poser une question avec plusieurs réponses possibles. 
    Si 'entry' est égal à "cursor", elle utilise `ask_question_cursor` (contrôle via les flèches). 
    Sinon, elle utilise `ask_question_kb` (contrôle via le clavier pour entrer des numéros).
    Elle retourne les indices des réponses sélectionnées sous forme d'une liste d'entiers (indices originaux).
    """
    
    # Si l'utilisateur choisit le mode "cursor", on utilise l'interface avec le curseur
    if entry == "cursor":
        return ask_question_cursor(question, answers)
    
    # Sinon, on utilise le mode de sélection par clavier (saisie de numéros)
    return ask_question_kb(question, answers)
