def lire_nombres(nom_fichier):
    nombres = []

    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            nombres.append(float(ligne.strip()))

    return nombres


def moyenne(nombres):
    return sum(nombres) / len(nombres)


def minimum(nombres):
    return min(nombres)


def maximum(nombres):
    return max(nombres)


def ecrire_resultats(nom_fichier, nombres):
    with open(nom_fichier, "w") as fichier:
        fichier.write(f"Moyenne : {moyenne(nombres):.2f}\n")
        fichier.write(f"Minimum : {minimum(nombres):.2f}\n")
        fichier.write(f"Maximum : {maximum(nombres):.2f}\n")


nombres = lire_nombres("notes.txt")

print(f"Moyenne : {moyenne(nombres):.2f}")
print(f"Minimum : {minimum(nombres):.2f}")
print(f"Maximum : {maximum(nombres):.2f}")

ecrire_resultats("resultats.txt", nombres)