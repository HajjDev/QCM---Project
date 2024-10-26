from ask_qcm_cursor import ask_qcm_cursor
from ask_qcm_kb import ask_qcm_kb

def ask_qcm(entry):
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
        return ask_qcm_cursor()
    
    # Sinon, on utilise le mode de sélection par clavier (saisie de numéros)
    return ask_qcm_kb()
