# Le jeu mystère

# Le but de cet exercice est de créer un jeu mystère dans lequel l'ordinateur choisit un nombre aléatoire entre 1 et 100, et l'utilisateur doit deviner ce nombre en un nombre limité de tentatives.

# Voici comment le jeu doit se dérouler :

# 1. L'ordinateur choisit un nombre aléatoire entre 1 et 100.
# 2. L'utilisateur a 10 tentatives pour deviner le nombre mystère.
# 3. À chaque tentative, l'utilisateur doit entrer un nombre.
# 4. Si le nombre entré par l'utilisateur est plus petit que le nombre mystère, l'ordinateur affiche "Le nombre mystère est plus grand !".
# 5. Si le nombre entré par l'utilisateur est plus grand que le nombre mystère, l'ordinateur affiche "Le nombre mystère est plus petit !".
# 6. Si le nombre entré par l'utilisateur est égal au nombre mystère, l'ordinateur affiche "Bravo, vous avez trouvé le nombre mystère en X tentatives !" (où X est le nombre de tentatives).
# 7. Si l'utilisateur n'a pas trouvé le nombre mystère après 10 tentatives, l'ordinateur affiche "Désolé, vous avez perdu ! Le nombre mystère était X." (où X est le nombre mystère).

# Voici un exemple d'exécution du jeu :

import random

nombre_mystere = random.randint(1, 100)

print("Bienvenue dans le jeu mystère !")
print("L'ordinateur a choisi un nombre mystère entre 1 et 100.")
print("Vous avez 10 tentatives pour le deviner.")

for i in range(1, 11):
    print(f"Tentative n°{i} :")
    nombre = int(input("Entrez un nombre :"))

    if nombre < nombre_mystere:
        print("Le nombre mystère est plus grand !")
    elif nombre > nombre_mystere:
        print("Le nombre mystère est plus petit !")
    else:
        print(f"Bravo, vous avez trouvé le nombre mystère en {i} tentatives !")
        break

if nombre != nombre_mystere:
    print(f"Désolé, vous avez perdu ! Le nombre mystère était {nombre_mystere}.")






