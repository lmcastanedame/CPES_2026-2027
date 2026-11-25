def lire_nombres(nom_fichier):
    nombres = []

    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            nombres.append(float(ligne.strip()))

    return nombres


def ecrire_resultats(nom_fichier, nombres, moyenne, minimum, maximum):
    with open(nom_fichier, "w") as fichier:
        fichier.write(f"Moyenne : {moyenne:.2f}\n")
        fichier.write(f"Minimum : {minimum:.2f}\n")
        fichier.write(f"Maximum : {maximum:.2f}\n")

if __name__ == "__main__":
    print("outil executé")