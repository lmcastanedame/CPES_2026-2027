# === CARNET DE TERRAIN ===
# Zone : Savane nord
# Température : 28.6 °C
# Espèces observées : ['girafe', 'tigre', 'singe', 'souris']
# Nombre d'espèces : 4
# Total d'animaux observés : 12
# Moyenne par espèce : 3.00


# 1

# print("=== CARNET DE TERRAIN ===")
# print("Zone : Savane nord")
# print("Température : 28.6 °C")

zone = "Savane nord"
temperature = 28.6


# print("=== CARNET DE TERRAIN ===")
# print(zone)
# print(temperature)
# mission_active = True























# 2

# 2 + 2
# "2" + "2"
# "ha" * 3
# "Température : " + 28.6




# str(28.6)
# type(28.6)
# type("28.6")



# 3

# print("Zone :", zone)
# print("Température :", temperature, "°C")

# print(f"Zone : {zone}")
# print(f"Température : {temperature} °C")

# print(f"Température : {temperature:.1f} °C")




# 4

# espece1 = "girafe"
# espece2 = "tigre"
# espece3 = "singe"
# espece4 = "souris"

especes = ["girafe", "tigre", "singe", "souris"]
# print(especes)

# print(especes[0])
# print(especes[1])
# print(especes[-1])
# print(especes[4])



# 5 

especes.append("lion")
# print(especes)
# print(len(especes))



# 6

observations = [4, 2, 5, 1, 3, 2]
nombre_especes = len(especes)
total_animaux = sum(observations)
minimum = min(observations)
maximum = max(observations)
moyenne = total_animaux / nombre_especes




# 7

print("\n=== CARNET DE TERRAIN ===")
print(f"Zone : {zone}")
print(f"Température : {temperature:.1f} °C")
print(f"Espèces observées : {especes}")
print(f"Nombre d'espèces : {nombre_especes}")
print(f"Total d'animaux observés : {total_animaux}")
print(f"Moyenne par espèce : {moyenne:.2f}")