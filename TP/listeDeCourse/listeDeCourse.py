# Dans ce projet, tu vas devoir créer un programme en ligne de commande qui permet de manipuler une liste de courses.

# Déroulé du script
# Le programme doit permettre de réaliser 5 actions :

# Ajouter un élément à la liste de courses

# Retirer un élément de la liste de courses

# Afficher les éléments de la liste de courses

# Vider la liste de courses

# Quitter le programme

# Tu dois donc demander à l'utilisateur de choisir parmi une de ces action en entrant un nombre de 1 à 5.

# Tu dois gérer le cas de figure où l'utilisateur ne rentre pas un nombre compris entre 1 et 5 ou s'il rentre par exemple des lettres ou un autre symbole invalide. Dans ce cas, tu dois afficher de nouveau le menu avec les options disponibles, jusqu'à ce que l'utilisateur choisisse une option valide.

# Dans ce projet, tu ne dois pas sauvegarder la liste dans un fichier ou une base de donnée.

# Le but ici est juste d'interagir avec l'utilisateur et de manipuler une liste en fonction de son choix.

# Bonne chance pour cet exercice ?

# Prends le temps de bien décrire toutes les étapes en français avant de te lancer dans le code !



# 1. Créer une liste vide
# 2. Afficher le menu
# 3. Demander à l'utilisateur de choisir une option
# 4. Si l'option est 1, demander à l'utilisateur d'ajouter un élément à la liste
# 5. Si l'option est 2, demander à l'utilisateur de retirer un élément de la liste
# 6. Si l'option est 3, afficher les éléments de la liste
# 7. Si l'option est 4, vider la liste
# 8. Si l'option est 5, quitter le programme
# 9. Si l'option n'est pas valide, afficher un message d'erreur et afficher de nouveau le menu
# 10. Répéter les étapes 2 à 9 jusqu'à ce que l'utilisateur choisisse de quitter le programme

# liste_de_course = []

# def afficher_menu():
#     print("1. Ajouter un élément à la liste de courses")
#     print("2. Retirer un élément de la liste de courses")
#     print("3. Afficher les éléments de la liste de courses")
#     print("4. Vider la liste de courses")
#     print("5. Quitter le programme")

# def ajouter_element():
#     element = input("Entrez un élément à ajouter à la liste de courses : ")
#     liste_de_course.append(element)
#     print("L'élément a bien été ajouté à la liste de courses !")

# def retirer_element():
#     element = input("Entrez un élément à retirer de la liste de courses : ")
#     if element in liste_de_course:
#         liste_de_course.remove(element)
#         print("L'élément a bien été retiré de la liste de courses !")
#     else:
#         print("L'élément n'est pas présent dans la liste de courses.")

# def afficher_elements():
#     print("Voici les éléments de la liste de courses :")
#     for element in liste_de_course:
#         print("- " + element)

# def vider_liste():
#     liste_de_course.clear()
#     print("La liste de courses a bien été vidée !")

# afficher_menu()

# while True:
#     choix = input("Entrez le numéro de l'action que vous souhaitez réaliser : ")
#     if choix == "1":
#         ajouter_element()
#     elif choix == "2":
#         retirer_element()
#     elif choix == "3":
#         afficher_elements()
#     elif choix == "4":
#         vider_liste()
#     elif choix == "5":
#         print("Merci d'avoir utilisé notre programme !")
#         break
#     else:
#         print("Veuillez entrer un numéro entre 1 et 5.")
#         afficher_menu()

import sys

LISTE = []

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICES:
        print("Veuillez choisir une option valide...")
        continue

    if user_choice == "1":  # Ajouter un élément
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")
    elif user_choice == "2":  # Retirer un élément
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif user_choice == "3":  # Afficher la liste
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")
    elif user_choice == "4":  # Vider la liste
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
    elif user_choice == "5":  # Quitter
        print("À bientôt !")
        sys.exit()

    print("-" * 50)