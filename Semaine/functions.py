def afficher_menu():
    print("--- Carnet de notes ---")
    print("1 - Ajouter une note")
    print("2 - Afficher les notes")
    print("3 - Afficher la moyenne")
    print("q - Quitter")

def note_est_valide(note):
    if note >= 0 and note <= 20:
        return True
    else:
        return False

def calculer_moyenne(notes):
    total = 0
    for note in notes:
        total = total + note
    moyenne = total / len(notes)
    print("Moyenne :", moyenne)