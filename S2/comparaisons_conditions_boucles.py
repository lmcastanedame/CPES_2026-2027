# 1

zone = "Savane nord"
temperature = 28.6
especes = ["girafe", "tigre", "singe", "souris"]
especes.append("lion")
observations = [4, 0, 5, 1, 7]
nombre_especes = len(especes)
total_animaux = sum(observations)
minimum = min(observations)
maximum = max(observations)
moyenne = total_animaux / nombre_especes

print("\n=== CARNET DE TERRAIN ===")
print(f"Zone : {zone}")
print(f"Température : {temperature:.1f} °C")
print(f"Espèces observées : {especes}")
print(f"Nombre d'espèces : {nombre_especes}")
print(f"Total d'animaux observés : {total_animaux}")
print(f"Moyenne par espèce : {moyenne:.2f}")
print("\n")

# girafe : 4 — observation fréquente
#  tigre : 0 — espèce non observée
#  singe : 5 — observation fréquente
# souris : 1 — espèce peu observée
#   lion : 7 — observation fréquente

print("*")
print("**")
print("***")
print("****")
print("*****")