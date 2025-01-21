#Résumé exercice 25


# Création d'une liste comprise entre 0 et 100 ses valeurs vont de -10 à + 40 cela dois afficher une alerte quand dans cette liste il y a + de 2 valeur négative "alerte ça caille" quand on a plus de 4 valeurs positives cad +20 degrés "alerte ça chauffe" sinon "la température est normale"

# Création d'une liste de 100 valeurs comprises entre -10 et 40
import random
liste = [random.randint(-10, 40) for i in range(100)]
print(liste)

# Comptage des valeurs négatives

compteur_negatif = 0
compteur_positif = 0

for i in liste:
    if i < 0:
        compteur_negatif += 1
    elif i > 20:
        compteur_positif += 1

if compteur_negatif > 2:
    print("Alerte ça caille")
elif compteur_positif > 4:
    print("Alerte ça chauffe")
# else:
#     print("La température est normale")

# Affichage du résultat

print(compteur_negatif)
print(compteur_positif)

#moyenne liste negative moyenne liste positive





  







