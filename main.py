from clear_console import clear_console
from ask_entry_mode import ask_entry_mode
from ask_qcm import ask_qcm
from ask_mode import ask_mode
from extract_questions import extract_qcm
from ask_question import ask_question
from calcul_point import calcul_point
from show_feedback import show_feedback
from after_qcm import after_qcm


def main():
    """
    pré: void
    post: void
    explication:
    Cette fonction `main` gère le déroulement d'un QCM interactif, depuis la sélection du mode d'entrée jusqu'à l'affichage des résultats.
    Elle propose à l'utilisateur de :
    - Sélectionner le mode d'entrée et le mode de calcul des points.
    - Choisir les réponses à chaque question.
    - Afficher un retour (feedback) et calculer les points obtenus.
    L'utilisateur peut ensuite choisir de refaire un autre QCM ou de quitter.
    """
    doQCM = True  # Contrôle la répétition du QCM

    # Boucle principale pour exécuter le QCM jusqu'à ce que l'utilisateur choisisse de quitter
    while doQCM:
        clear_console()  # Efface la console pour un affichage propre
        
        entry = ask_entry_mode()  # Demande à l'utilisateur de choisir le mode d'entrée (clavier ou curseur)
        
        clear_console()  # Efface de nouveau la console
        
        questions = ask_qcm(entry)  # Charge les questions du QCM
        if questions is False:
            print("Erreur lors du chargement du QCM. Veuillez réessayer.")
            continue  # Redémarre la boucle si le QCM n'est pas chargé

        mode = ask_mode(entry)  # Demande à l'utilisateur de choisir le mode de calcul des points

        # Liste pour stocker les réponses données par l'utilisateur pour chaque question
        answered = []
        for question in questions:
            # Extrait la question et les réponses pour l'affichage
            formatted = extract_qcm(question)
            q_title = formatted[0]  # Texte de la question
            q_answers = formatted[1]  # Liste des réponses possibles

            # Pose la question et récupère les indices des réponses sélectionnées
            index_answer = ask_question(entry, q_title, q_answers)
            answered.append(index_answer)  # Stocke les indices des réponses choisies pour chaque question
            
        show_feedback(questions, answered)  # Affiche le feedback à l'utilisateur sur ses réponses
        calcul_point(mode, questions, answered)  # Calcule et affiche les points obtenus selon le mode choisi
        doQCM = after_qcm()  # Demande à l'utilisateur s'il souhaite refaire un QCM


if __name__ == "__main__":
    main()
