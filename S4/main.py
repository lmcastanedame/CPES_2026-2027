from stats import moyenne, minimum, maximum
from outil import lire_nombres, ecrire_resultats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nombres = lire_nombres("notes.txt")

print(f"Moyenne : {moyenne(nombres):.2f}")
print(f"Minimum : {minimum(nombres):.2f}")
print(f"Maximum : {maximum(nombres):.2f}")

ecrire_resultats("resultats.txt", nombres, moyenne(nombres), minimum(nombres), maximum(nombres))