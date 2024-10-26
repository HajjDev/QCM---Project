import random
from clear_console import clear_console

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

def ask_question_kb(question, answers):
    """
    pré: question, str; answers, list of str
    post: selected_indices, list of int
    explication:
    Cette fonction affiche une question avec plusieurs réponses possibles, mélangées, et demande à l'utilisateur 
    de sélectionner les réponses en entrant une liste de numéros séparés par des tirets (ex: 1-2-3).
    Elle vérifie la validité de la saisie (nombres valides, sans doublons) et retourne les indices des réponses sélectionnées 
    dans la liste originale.
    """

    answered = False  # Indicateur pour savoir si la question a reçu une réponse valide
    message2show = ""  # Message à afficher en cas d'erreur d'entrée

    # Sauvegarder la liste des réponses d'origine
    original_answers = answers.copy()
  
    # Mélanger les réponses aléatoirement
    random.shuffle(answers)

    # Boucle jusqu'à ce qu'une réponse valide soit fournie
    while not answered:
        clear_console()  # Efface la console pour un affichage propre

        # Afficher le message d'erreur s'il y en a un
        if message2show:
            print(message2show)

        # Afficher la question
        print(question)

        # Afficher la liste des réponses mélangées
        for i in range(len(answers)):
            print(f"{i + 1}. {answers[i]}")  # Affiche chaque réponse avec son numéro

        print("\n")
        # Demande à l'utilisateur de saisir une ou plusieurs réponses
        answer_input = input("Choisissez votre réponse (ex: 1-2-3): \n")
        answer_indices = answer_input.split("-")  # Divise les réponses saisies

        toReturn = []  # Liste des indices originaux des réponses choisies
        valid_input = True  # Indicateur pour valider la saisie

        # Vérification de la validité des réponses données par l'utilisateur
        for a in answer_indices:
            try:
                index = int(a) - 1  # Convertit l'entrée utilisateur en un index de liste (0-based)
                if index < 0 or index >= len(answers):
                    message2show = "Veuillez entrer un numéro de réponse valide."
                    valid_input = False  # Invalide la saisie si l'index est hors limite
                    break
                # Utilise `true_index` pour retrouver l'index original de la réponse
                toReturn.append(true_index(answers[index], original_answers))
            except ValueError:
                message2show = "Ce n'est pas un chiffre. Veuillez entrer un numéro correct."
                valid_input = False  # Invalide la saisie si l'entrée n'est pas un nombre
                break

        # Vérification des doublons dans les réponses
        if valid_input and contain_similar_elements(toReturn):
            message2show = "Pas de doublons autorisés. Veuillez entrer des numéros uniques."
            valid_input = False

        # Si la saisie est valide, on retourne les indices originaux des réponses sélectionnées
        if valid_input:
            answered = True
            return toReturn  # Retourne la liste des indices des réponses sélectionnées
