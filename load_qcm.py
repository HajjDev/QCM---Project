import qcm

def load_qcm(filename):
    """
    pré: filename, str
    post: questions, list or bool
    explication:
    Cette fonction tente de charger un fichier QCM en appelant `qcm.build_questionnaire(filename)`.
    Elle ajoute automatiquement l'extension `.txt` au nom de fichier fourni.
    En cas de succès, elle retourne une liste de questions. 
    Si une exception est levée (par exemple, fichier introuvable ou problème de lecture), elle retourne `False`.
    """
    
    filename += ".txt"  # Ajoute l'extension .txt au nom de fichier

    try:
        # Tente de charger les questions depuis le fichier avec qcm.build_questionnaire
        questions = qcm.build_questionnaire(filename)
        return questions  # Retourne la liste de questions si chargement réussi
    except Exception:
        # Retourne False en cas d'échec (fichier non trouvé ou erreur de chargement)
        return False
