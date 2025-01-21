# EXERCICE 11
# Écrivez un programme pour trouver le plus petit parmi quatre nombres en utilisant des structures conditionnelles.
# Entrée : 10, 25, 5, 17
# Sortie : 5

dix = 10
vingtCinq = 25
cinq = 5
dixSept = 17

if dix < vingtCinq and dix < cinq and dix < dixSept:
    print(dix)
elif vingtCinq < dix and vingtCinq < cinq and vingtCinq < dixSept:
    print(vingtCinq)
elif cinq < dix and cinq < vingtCinq and cinq < dixSept:
    print(cinq)
else:
    print(dixSept)




# EXERCICE 12
# Écrivez un programme pour vérifier si une température donnée est froide, modérée ou chaude.

# Température < 10 : froide
# Température entre 10 et 25 : modérée
# Température > 25 : chaude
# Entrée : 15
# Sortie : La température est modérée.


temperature = 8

if (temperature < 10):
    print("La température est froide. 🥶")
elif (temperature >= 10 and temperature <= 25):
    print("La température est modérée. 😊")
else:
    print("La température est chaude. 🥵")





# EXERCICE 13
# Écrivez un programme pour vérifier si un nombre est positif, négatif ou égal à zéro.
# Entrée : -5
# Sortie : -5 est un nombre négatif.

nb = -5

if nb > 0:
    print(f"{nb} est un nombre positif.")
elif nb < 0:
    print(f"{nb} est un nombre négatif.")



# EXERCICE 14
# Écrivez un programme pour vérifier si une personne est admissible à voter ou non.
# Une personne est admissible si son âge est supérieur ou égal à 18 ans.
# Entrée : 20
# Sortie : Vous êtes admissible à voter.


age = 20

if age >= 18:
    print("Vous êtes admissible à voter.")
else:
    print("Vous n'êtes pas admissible à voter.")





# EXERCICE 15
# Écrivez un programme pour entrer une note d'examen (sur 20) et afficher la mention correspondante.

# Note >= 16 : Très bien
# Note >= 12 : Bien
# Note >= 8 : Passable
# Note < 8 : Insuffisant
# Entrée : 14
# Sortie : Mention Bien


# note = int (input("Entrez votre note: "))

# if note >= 16:
#     print("Très bien")
# elif note >= 12:
#     print("Bien")
# elif note >= 8:
#     print("Passable")
# else:
#     print("Insuffisant")




# EXERCICE 16
# Écrivez un programme pour vérifier si un triangle est valide ou non à l'aide des trois longueurs de ses côtés.
# Un triangle est valide si la somme de deux côtés est toujours supérieure au troisième côté.
# Entrée : 7, 10, 5
# Sortie : C'est un triangle valide.


# cote1 = int(input("Entrez le premier côté: "))
# cote2 = int(input("Entrez le deuxième côté: "))
# cote3 = int(input("Entrez le troisième côté: "))
# if cote1 + cote2 > cote3 or cote1 + cote3 > cote2 or cote2 + cote3 > cote1:
#     print("C'est un triangle valide.")
# else:
#     print("C'est un triangle invalide.")



# EXERCICE 17
# Écrivez un programme pour déterminer si un nombre donné est un multiple de 5, 7 ou aucun des deux.
# Entrée : 35
# Sortie : 35 est un multiple de 5 et de 7.

nombre = 35

if nombre % 5 == 0 and nombre % 7 == 0:
    print(f"{nombre} est un multiple de 5 et de 7.")
elif nombre % 5 == 0:    
    print(f"{nombre} est un multiple de 5.")
elif nombre % 7 == 0:
    print(f"{nombre} est un multiple de 7.")
else:
    print(f"{nombre} n'est pas un multiple de 5 ni de 7.")



# EXERCICE 18
# Écrivez un programme pour afficher le type de triangle (équilatéral, isocèle ou scalène) selon les longueurs de ses trois côtés.

# Équilatéral : Tous les côtés sont égaux.
# Isocèle : Deux côtés sont égaux.
# Scalène : Tous les côtés sont différents.
# Entrée : 5, 5, 8
# Sortie : C'est un triangle isocèle.

cote1 = 5
cote2 = 5
cote3 = 8

if cote1 == cote2 and cote2 == cote3:
    print("C'est un triangle équilatéral.")
elif cote1 == cote2 or cote1 == cote3 or cote2 == cote3:
    print("C'est un triangle isocèle.")
else:
    print("C'est un triangle scalène.")




# EXERCICE 19
# Écrivez un programme pour vérifier si une personne est en sous-poids, poids normal ou en surpoids à l'aide de son IMC (Indice de Masse Corporelle).


# IMC < 18.5 : Sous-poids
# IMC entre 18.5 et 24.9 : Poids normal
# IMC >= 25 : Surpoids
# Entrée : IMC = 22
# Sortie : Poids normal

imc = 22

if imc < 18.8:
    print("Sous-poids")
elif imc >= 18.5 and imc <= 24.9:
    print("Poids normal")
else:
    print("Surpoids")



# EXERCICE 20
# Écrivez un programme pour convertir une note de lettre en note numérique.

# A : 90-100
# B : 80-89
# C : 70-79
# D : 60-69
# F : <60
# Entrée : B
# Sortie : La plage de la note est 80-89.


note_lettre = "D"

if note_lettre == "A":
    print("La plage de la note est 90-100.")
elif note_lettre == "B":
    print("La plage de la note est 80-89.")
elif note_lettre == "C":
    print("La plage de la note est 70-79.")
elif note_lettre == "D":
    print("La plage de la note est 60-69.")
else:
    print("La plage de la note est <60.")






# EXERCICE 21 : Calculatrice avancée
# Écrivez un programme qui demande à l'utilisateur d'entrer deux nombres et une opération mathématique (+, -, *, /, %) et effectue l'opération correspondante.

# Si l'utilisateur entre une opération non valide, affichez un message d'erreur.
# Entrée : 15, 3, '/'
# Sortie : Résultat = 5


# nombre1 = int(input("Entrez le premier nombre: "))
# operation = input("Entrez l'opération: ")
# nombre2 = int(input("Entrez le deuxième nombre: "))

# if operation == "+":
#     print(f"Résultat = {nombre1 + nombre2}")
# elif operation == "-":
#     print(f"Résultat = {nombre1 - nombre2}")
# elif operation == "*":
#     print(f"Résultat = {nombre1 * nombre2}")
# elif operation == "/":
#     print(f"Résultat = {nombre1 / nombre2}")









# EXERCICE 22 : Tri des nombres
# Écrivez un programme pour entrer trois nombres et les afficher en ordre croissant.
# Entrée : 45, 12, 78
# Sortie : 12, 45, 78



# premier = int(input("Entrez le premier nombre: "))
# deuxieme = int(input("Entrez le deuxième nombre: "))
# troisieme = int(input("Entrez le troisième nombre: "))
# if premier > deuxieme:
#     premier, deuxieme = deuxieme, premier
# if premier > troisieme:
#     premier, troisieme = troisieme, premier
# if deuxieme > troisieme:
#     deuxieme, troisieme = troisieme, deuxieme
# print(premier, deuxieme, troisieme)







# EXERCICE 23 : Calcul des notes finales
# Écrivez un programme pour entrer les notes de plusieurs matières (par exemple : mathématiques, physique, chimie), calculer la moyenne et déterminer si l'élève est admis ou non :

# Moyenne >= 10 : admis
# Moyenne < 10 : non admis
# Entrée : 12, 8, 15
# Sortie : Moyenne = 11.67, Résultat = Admis

math = 12
physique = 8
chimie = 15

moyenne = (math + physique + chimie) / 3

if moyenne >= 10:
    print(f"Moyenne = {moyenne}, Résultat = Admis")
else:
    print(f"Moyenne = {moyenne}, Résultat = Non admis")









# EXERCICE 24 : Classification des triangles avancée
# Ajoutez une vérification supplémentaire à l'exercice précédent (triangle valide) pour déterminer si le triangle est :

# Rectangle (respecte le théorème de Pythagore).
# Non rectangle.
# Entrée : 3, 4, 5
# Sortie : Triangle rectangle.











# EXERCICE 25 : Vérification des mots de passe
# Écrivez un programme pour demander à l'utilisateur de créer un mot de passe, puis de le vérifier.

# Le mot de passe doit contenir au moins 8 caractères, inclure au moins une majuscule, un chiffre et un caractère spécial.
# Affichez si le mot de passe est valide ou non.
# Entrée : P@ssword123
# Sortie : Mot de passe valide.
# EXERCICE 26 : Année bissextile sur une plage d'années
# Demandez à l'utilisateur une plage d'années (par exemple, 2000 à 2020) et affichez toutes les années bissextiles de cette plage.
# Entrée : 2000, 2020
# Sortie : Années bissextiles : 2000, 2004, 2008, 2012, 2016, 2020.

# EXERCICE 27 : Conversion des unités de température
# Écrivez un programme qui demande à l'utilisateur d'entrer une température en degrés Celsius ou Fahrenheit et de convertir cette température dans l'autre unité.
# Formules :

# De Celsius à Fahrenheit : 
# 𝐹
# =
# 𝐶
# ×
# 9
# 5
# +
# 32
# F=C× 
# 5
# 9
# ​
#  +32
# De Fahrenheit à Celsius : 
# 𝐶
# =
# (
# 𝐹
# −
# 32
# )
# ×
# 5
# 9
# C=(F−32)× 
# 9
# 5
# ​
 
# Entrée : 100°C
# Sortie : 212°F
# EXERCICE 28 : Conversion des heures au format 12h/24h
# Écrivez un programme qui demande à l'utilisateur une heure au format 24h et la convertit au format 12h, ou vice versa.
# Entrée : 14:30 (format 24h)
# Sortie : 2:30 PM

# EXERCICE 29 : Numéro de téléphone valide
# Écrivez un programme pour vérifier si un numéro de téléphone entré par l'utilisateur est valide :

# Il doit comporter exactement 10 chiffres.
# Il doit commencer par un chiffre entre 6 et 9.
# Entrée : 9876543210
# Sortie : Numéro valide.
# EXERCICE 30 : Jeu : Deviner un nombre
# Écrivez un programme où l'ordinateur choisit un nombre au hasard entre 1 et 100, et l'utilisateur doit deviner ce nombre. Le programme donne des indices :

# "Plus grand" ou "Plus petit" selon le cas.
# Arrêtez une fois que le nombre est trouvé.
# Entrée : 50 (tentative utilisateur), 75 (tentative utilisateur), 70 (tentative utilisateur)
# Sortie : Félicitations, vous avez trouvé le nombre : 70






