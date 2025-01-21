import random

# Initialisation des listes

temp = []
liste_valeurs_positives = []
liste_valeurs_negatives = []
liste_valeurs_normales = []

# Génération et tri de 100 températures aléatoires
for i in range(100):
    temp.append(random.randint(-10, 41))

temp.sort()

# Classification des températures en listes distinctes
for i in temp:
    if i < 0:
        liste_valeurs_negatives.append(i)
    elif 0 <= i < 20:
        liste_valeurs_normales.append(i)
    else:
        liste_valeurs_positives.append(i)

# Alerte basée sur les valeurs des listes
if len(liste_valeurs_negatives) > 2:
    print("Alerte : Attention ca caille")
elif len(liste_valeurs_positives) > 4:
    print("Alerte : Attention met de la crème")

# Extraction des températures minimale et maximale
temp_min = temp[0]
temp_max = liste_valeurs_positives[-1] if liste_valeurs_positives else temp[-1]

# Affichage des résultats
print(f"Temperature maximale : {temp_max}°")
print(f"Temperature minimale : {temp_min}°")
print("--------------------------------------------------------")        
print(f"Valeur de la liste positive : {liste_valeurs_positives}")
print(f"Valeur de la liste négative : {liste_valeurs_negatives}")
print(f"Valeur de la liste normale : {liste_valeurs_normales}")

# Tri des listes de valeurs positives et négatives
liste_valeurs_positives.sort()
liste_valeurs_negatives.sort()

print(f"Valeurs positives triées : {liste_valeurs_positives}")
print(f"Valeurs négatives triées : {liste_valeurs_negatives}")

# Calcul de la somme et de la moyenne des valeurs positives et négatives
somme_valeurs_positives = sum(liste_valeurs_positives)
somme_valeurs_negatives = sum(liste_valeurs_negatives)

print(f"La somme des valeurs positives est de : {somme_valeurs_positives}")
print(f"La somme des valeurs négatives est de : {somme_valeurs_negatives}")

moyenne_valeurs_positives = somme_valeurs_positives / len(liste_valeurs_positives) if liste_valeurs_positives else 0
moyenne_valeurs_negatives = somme_valeurs_negatives / len(liste_valeurs_negatives) if liste_valeurs_negatives else 0

print(f"La moyenne des valeurs positives est de : {moyenne_valeurs_positives}")
print(f"La moyenne des valeurs négatives est de : {moyenne_valeurs_negatives}")

# Fonction pour générer une liste de 100 valeurs aléatoires entre -10 et 41
def create_liste():
    liste = [random.randint(-10, 41) for _ in range(100)]
    return liste

print(create_liste())