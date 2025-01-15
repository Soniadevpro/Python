# Description: Exercices sur les boucles
# Version: 1.0
# Votre script dois afficher les chaines de caracteres suivantes 
# Utilisateur 1
# Utilisateur 2
# Utilisateur 3
# Utilisateur 4
# Utilisateur 5
# Utilisateur 6
# Utilisateur 7
# Utilisateur 8
# Utilisateur 9
# Utilisateur 10
# Votre script doit bien commencer à l'utilisateur 1 et non 0 !


for i in range(1, 11):
    print("Utilisateur", i)


#Affiche les lettres du mot Python a l'envers

mot = "Python"
for i in range(len(mot) - 1, -1, -1): # On commence à la fin de la chaine de caractères et on remonte jusqu'au début de la chaine de caractères
    print(mot[i])



    # afficher la table de multiplication du nombre 7

nombre =7 
for i in range(1, 11):
    print(i, "x", nombre, "=", i * nombre)


continuer = "o"
while continuer == "o":
    print("on continue...")
    continuer = input("voulez vous continuer ? o/n : ")


#remplacer des boucles par des comprehensions de liste

liste = [ -1, -2, 3, 4, 5 ]
liste_nb_positifs = [ i * 2 for i in liste if i > 0 ]

print(liste_nb_positifs)


# afficher les nombres pairs de la variable nombres = range(51)

nombres = range(51)
nombres_pairs = [ i for i in nombres if i % 2 == 0 ]
print(nombres_pairs)