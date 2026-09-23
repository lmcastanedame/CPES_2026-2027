from functions import afficher_menu, note_est_valide, calculer_moyenne

notes = []
choix = ""

while choix != "q":
    afficher_menu()

    choix = input("Votre choix : ")

    if choix == "1":
        note = float(input("Note : "))
        if note_est_valide(note):
            notes.append(note)
        else:
            print("Note invalide")

    elif choix == "2":
        if len(notes) == 0:
            print("Aucune note")
        else:
            for note in notes:
                print(note)

    elif choix == "3":
        if len(notes) == 0:
            print("Aucune moyenne disponible")
        else:
            calculer_moyenne(notes)

    elif choix == "q":
        print("Au revoir")

    else:
        print("Choix inconnu")