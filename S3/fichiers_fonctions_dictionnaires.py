# moyenne : 12.55
# admis : 14
# recalés : 5
# notes invalides : 1

# notes2.txt
# 13.5 admis
# 17.0 admis
# 9.5 recalé
# ...
# 29.0 invalide

# with open("notes.txt", "r") as fichier:
#     ligne = fichier.readline()

# print(ligne)
# print(type(ligne))
# print(repr(ligne))
# ligne = ligne.strip()
# note = float(ligne)
# print(note)
# print(type(note))

def lire_notes(nom_fichier):

    notes = []
    with open(nom_fichier, "r") as fichier:
        lignes = fichier.readlines()
        
    for ligne in lignes:
        note = float(ligne.strip())
        notes.append(note)
        
    return notes

def statut_note(note):
    if note < 0 or note > 20:
        return "invalide"
    if note >= 10:
        return "admis"
    return "recalé"

notes = lire_notes("notes.txt")
# print(notes)

bilan = {
    "admis": 0,
    "recalé": 0,
    "invalide": 0
}

for note in notes:
    statut = statut_note(note)
    bilan[statut] += 1

for statut, nombre in bilan.items():
    print(f"{statut} : {nombre}")

notes_valides = []
for note in notes:
    if statut_note != "invalide":
        notes_valides.append(note)
moyenne = sum(notes_valides) / len(notes_valides)
print(f"{moyenne:.2f}")

with open("notes2.txt", "w") as fichier:
    for note in notes:
        statut = statut_note(note)
        fichier.write(f"{note:.1f} {statut}\n")