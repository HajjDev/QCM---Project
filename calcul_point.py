def nbr_of_correct_answers(questions, index):
    """
    pré: questions, list of list; index, int
    post: compteur, int
    explication:
    Cette fonction compte le nombre de réponses corecctes pour une question donnée.
    Elle prends en entrée 'questions', une liste rrépsentant les questions et 'index", l'inidece de la réponse dans la liste.
    Retourn un entier 'compteur' représentant le nombre de réponses correctes.
    """
    compteur = 0 # Initialisation du compteur de réponses correctes
    # Parcours des réponses pour la question spécifiée
    for answer in questions[index][1]:
        if answer[1]: # Si la réponse est correcte
            compteur += 1
    return compteur # Retourne le nombre de réponses correctes


def calcul_point(mode, questions, answers):
    """
    pré: questions, list of list; answer, list of list of bool
    post: void
    explication:
    Cette fonction calcule les points ibtenus par questions dans 3 modes de cotatiolns:
    - Mode normal : points propotionnels aux bonnes réponses (pas de punitions pour les mauvaises).
    - Mode éliminatoire : pénalité pour les erreurs.
    - Mode adaptif : points ajustés selon les réponses correctes et erreurs.
    Et affiche de manière structurer les points de l'utilisateur 
    """

    ORANGE = "\033[38;5;214m"
    BLUE = "\033[34m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    TEXT_BLACK = "\033[30m"
    HIGHLIGHT_WHITE = "\033[47m"
    RESET = "\033[0m"
    
    points_normal = 0
    points_eliminatoire = 0
    points_adaptif = 0  # Pour le mode adaptatif
    note = 0

    for index in range(len(questions)):
        nbre_correct = nbr_of_correct_answers(questions, index)
        compteur_correct = 0
        compteur_erreur = 0

        # Parcours des réponses choisies pour la question actuelle
        for sub_index in range(len(answers[index])):
            question_answer = questions[index][1][answers[index][sub_index]]
            is_correct = question_answer[1]

            # Mode normal
            if is_correct:
                compteur_correct += 1
                points_normal += 1 / nbre_correct  # Récompense pour chaque bonne réponse
                points_adaptif += 1 / nbre_correct  # Récompense adaptative pour chaque bonne réponse
            else:
                compteur_erreur += 1  # Comptage des erreurs pour le mode adaptif

        # Mode éliminatoire
        if compteur_erreur > 0 or compteur_correct < nbre_correct:
            points_eliminatoire -= 1  # Pénalité si mauvaise réponse ou omission
            points_adaptif -= (compteur_erreur + (nbre_correct - compteur_correct)) / nbre_correct  # Pénalité adaptative
        else:
            points_eliminatoire += 1  # Ajout de point si toutes les réponses correctes sont choisies
    
    if mode == 'Normal':
        note = points_normal
    elif mode == 'Éliminatoire':
        note = max(0, points_eliminatoire)
    elif mode == 'Adaptif':
        note = max(0, points_adaptif)
    
    print("-------------------------------------------------------------------")
    if not mode == 'Comparatif':
        print(f"""
{ORANGE}Selon les conditions du mode que vous avez choisi, vous avez obtenu{RESET}:

Nombre de questions : {BLUE} {len(questions)} {RESET}
Vous avez choisi le mode {BLUE}{mode}{RESET} donc : 
{GREEN}Note finale {RESET}: {note} / {len(questions)}
""")
    else:
        print(f"""
{ORANGE}Selon les conditions du mode que vous avez choisi, vous avez obtenu{RESET}:

Nombre de questions : {BLUE} {len(questions)} {RESET}
Vous avez choisi le mode {BLUE}Comparatif{RESET} donc, {GREEN}Note finale {RESET}: 

Mode Normal : {points_normal} / {len(questions)}
Mode Éliminatoire : {points_normal} / {len(questions)}
Mode Adaptif : {points_adaptif} / {len(questions)}
""")

    print("-------------------------------------------------------------------")


