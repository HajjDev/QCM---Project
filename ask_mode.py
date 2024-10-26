from ask_mode_cursor import ask_mode_cursor
from ask_mode_kb import ask_mode_kb

def ask_mode(entry):
    """
    pré: entry, str (doit être "cursor" ou "kb")
    post: mode, char
    explication:
    Cette fonction permet de choisir un mode d'interaction pour sélectionner un mode de QCM.
    En fonction de l'entrée `entry`, elle appelle soit `ask_mode_cursor` (pour le contrôle avec curseur),
    soit `ask_mode_kb` (pour le contrôle via clavier).
    Retourne une chaîne de caractères représentant le mode sélectionné par l'utilisateur, parmi "Normal",
    "Eliminatoire", "Adaptif", ou "Comparatif".
    """

    if entry == "cursor":
        return ask_mode_cursor()  # Appelle la fonction de sélection avec curseur
    return ask_mode_kb()  # Par défaut, utilise la sélection via clavier
