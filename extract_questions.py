def extract_qcm(question):
    """
    pré: question, tuple
    post: tuple, (str, list of str)
    explication:
    Cette fonction extrait la question et les réponses associées d'un tuple représentant un QCM. 
    Elle prend en entrée un tuple 'question', où le premier élément est la question (str) 
    et le deuxième est une liste de tuples représentant les réponses possibles (chaque sous-tuple contient une réponse et un indicateur de correction).
    La fonction retourne un tuple contenant la question sous forme de chaîne de caractères et une liste des réponses (sans indicateur de correction).
    """
    
    extract_anwers = []           # Liste pour stocker les réponses extraites
    extract_question = question[0] # La question est le premier élément du tuple d'entrée

    # Parcourt les réponses et extrait uniquement le texte de chaque réponse
    for el in question[1]:
        extract_anwers.append(el[0])
    
    return (extract_question, extract_anwers)  # Retourne un tuple (question, réponses extraites)
