import random
temp = []
liste_valeurs_positives = []
liste_valeurs_negatives = []
liste_valeurs_normales = []

for i in range(100):
    temp.append(random.randint(-10,41))

temp.sort()

for i in temp:
    if(i<0):
        liste_valeurs_negatives.append(i)
    elif(0 <= i < 20):
        liste_valeurs_normales.append(i)
    else:
        liste_valeurs_positives.append(i)

if(len(liste_valeurs_negatives) > 2):
    print("Alerte : Attention ca caille")

if(len(liste_valeurs_positives) > 4):
    print("Alerte : Attention met de la crème")    

temp_min = temp[0]
temp_max = liste_valeurs_positives[-1]

print(f"Temperature maximale : {temp_max}°")
print(f"Temperature minimale : {temp_min}°")
print("--------------------------------------------------------")        
print(f"Valeur de la liste positive : {liste_valeurs_positives}")
print(f"Valeur de la liste négative : {liste_valeurs_negatives}")
print(f"Valeur de la liste normale : {liste_valeurs_normales}")


# fonction creation liste
def create_liste_temp():
    temp = []
    for i in range(100):
        temp.append(random.randint(-10,41))
    return temp

help(create_liste_temp)
# fonction tri liste
def sort_liste_temp(temp):
    temp.sort()

    help(sort_liste_temp)
    return temp
# fonction tri des valeurs
def get_liste_valeurs(temp):
    liste_valeurs_positives = []
    liste_valeurs_negatives = []
    liste_valeurs_normales = []

    for i in temp:
        if(i<0):
            liste_valeurs_negatives.append(i)
        elif(0 <= i < 20):
            liste_valeurs_normales.append(i)
        else:
            liste_valeurs_positives.append(i)
    return liste_valeurs_positives, liste_valeurs_negatives, liste_valeurs_normales
help(get_liste_valeurs)

# fonction alerte valeur chaud froid

def alerte(liste_valeurs_positives, liste_valeurs_negatives):
    if(len(liste_valeurs_negatives) > 2):
        print("Alerte : Attention ca caille")

    if(len(liste_valeurs_positives) > 4):
        print("Alerte : Attention met de la crème")
help(alerte)

# fonction valeur min et max

def get_temp_min(temp):
    return temp[0]

def get_temp_max(liste_valeurs_positives):
    return liste_valeurs_positives[-1]


# Programme principal

temp = create_liste_temp()

temp = sort_liste_temp(temp)

liste_valeurs_positives, liste_valeurs_negatives, liste_valeurs_normales = get_liste_valeurs(temp)

alerte(liste_valeurs_positives, liste_valeurs_negatives)

temp_min = get_temp_min(temp)
temp_max = get_temp_max(liste_valeurs_positives)

print(f"Temperature maximale : {temp_max}°")
print(f"Temperature minimale : {temp_min}°")
print("--------------------------------------------------------")
print(f"Valeur de la liste positive : {liste_valeurs_positives}")
print(f"Valeur de la liste négative : {liste_valeurs_negatives}")
print(f"Valeur de la liste normale : {liste_valeurs_normales}")




# fonction helper pour les fonctions précédentes


    


