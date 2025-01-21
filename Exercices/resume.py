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

elif(len(liste_valeurs_positives) > 4):
    print("Alerte : Attention met de la crème")    

temp_min = temp[0]
temp_max = liste_valeurs_positives[-1]

print(f"Temperature maximale : {temp_max}°")
print(f"Temperature minimale : {temp_min}°")
print("--------------------------------------------------------")        
print(f"Valeur de la liste positive : {liste_valeurs_positives}")
print(f"Valeur de la liste négative : {liste_valeurs_negatives}")
print(f"Valeur de la liste normale : {liste_valeurs_normales}")







  







