from load_qcm import load_qcm

def ask_qcm_kb():
    """
    pré: void
    post: questions_charges, list or None
    explication:
    Cette fonction demande à l'utilisateur de saisir le nom d'un fichier contenant un QCM (sans l'extension .txt).
    Elle appelle la fonction `load_qcm` pour charger les questions depuis le fichier spécifié.
    Si le fichier est invalide (non trouvé ou incorrect), elle continue de redemander un nom de fichier jusqu'à ce qu'un fichier valide soit fourni.
    Retourne une liste de questions si le fichier est valide, sinon continue la boucle.
    """
    
    answered = False  # Indicateur pour savoir si un fichier valide a été fourni
    questions_charges = None  # Contiendra les questions chargées depuis le fichier

    # Boucle pour demander à l'utilisateur de fournir un nom de fichier jusqu'à ce qu'un fichier valide soit trouvé
    while not answered:
        # Demande le nom du fichier sans l'extension .txt
        nom_fichier = input("Ecrivez le nom du fichier. (Il ne faut pas inclure le .txt): ")
        # Charge le QCM à partir du fichier spécifié
        questions_charges = load_qcm(nom_fichier)

        # Vérifie si le fichier est invalide (si load_qcm renvoie False)
        if questions_charges == False:
            print("Le nom du fichier est invalide.")  # Message d'erreur si le fichier est incorrect
        else:
            answered = True  # Fichier valide trouvé, on peut sortir de la boucle
    
    return questions_charges  # Retourne les questions chargées
