# La boucle while en Python permet d'exécuter un bloc de code tant qu'une condition est vraie. C'est une structure de contrôle utilisée pour répéter une action jusqu'à ce qu'une condition cesse d'être satisfaite.


# Exemple simple de boucle while
# Voici un exemple simple de boucle while en Python :

# i = 0
# while i <= 5:
#     print(i)
#     i += 1

# Dans cet exemple, la variable i est initialisée à 0. La boucle while est exécutée tant que i est inférieur à 5. À chaque itération, la valeur de i est affichée avec print(i) et incrémentée de 1 avec i += 1. La boucle s'arrête lorsque i atteint 5.

# Sortie :
# 0

# chaine = "Je ne copierai plus sur mon voisin.\n"
# i = 1
# while  i <= 10:
#     print(i, chaine)
#     i += 1

   
# exercice 1 écrire et sauver un programme 14_nombrespairs qui affichera les nombres pairs (2,4,6,8) de 2 à 40

# a = 2
# while a <= 40:
#     print(f"{a} ", end="/_")
#     a += 2



# Exercice 2 le juste prix
# écrire et sauver un programme qui va 
# choisir un prix au hasard (à valeur entière) entre 1 et 100
# demander à l'utilisateur de deviner le prix
# à chaque réponse incorrecte de l'utilisateur, lui répondre : c'est plus ou c'est moins
# une fois la bonne réponse trouvée, lui réponde "Bravo, vous avez trouvé le juste prix !"


# from random import randint

# prix = randint(1, 100)

# trouve = False
# while not trouve:

#     reponse = int(input("Devinez le prix (entre 1 et 100) : "))
#     if reponse < prix:
#         print("C'est plus !")
#     elif reponse > prix:
#         print("C'est moins !")
#     else:
#         print("Bravo, vous avez trouvé le juste prix !")
#         trouve = True



# propagation d'une épidémie (ou d'une rumeur)

# Les chercheurs s'intéresse à la vitesse de propagation d'une dépidémie au sein d'une commune donnée, et donc à la vitesse à laquelle 
# mesures sanitaires ont devoir être prises pour éviter une catastrophe.


# Votre programme doit d'abord lire un nombre n correspondant à la population totale de la ville.
# Sachant qu'une personne était malade au jour 1 dans la ville et que chaque jour 3 personnes supplémentaires sont contaminées, votre programme doit afficher le jour à partir duquel la population de la ville sera entièrement contaminée.



# nb_habitant = 15000
# nb_malade = 1
# jour = 1

# while nb_malade < nb_habitant:
#     nb_malade += 3
#     jour += 1

# print(f"La ville sera entièrement contaminée au jour {jour}")




# from math import pow
# import tkinter as tk

# def contamination_pow():

#     nb_habitant = 15000  # Nombre total d'habitants
#     nb_malade = 1        # Nombre initial de malades
#     jour = 0             # Compteur de jours

#     while nb_malade < nb_habitant:
#         jour += 1
#         nb_malade = pow(3, jour)  # Calcul exponentiel : chaque jour, les malades triplent

#     print(f"La ville sera entièrement contaminée au jour {jour}")



# def contamination (): 
#     nb_habitant = 15000  # Nombre total d'habitants
#     nb_malade = 1        # Nombre initial de malades
#     jour = 0             # Compteur de jours

#     while nb_malade < nb_habitant:
#         nb_malade *= 3  # Chaque personne malade contamine 3 autres personnes
#         jour += 1

#     print(f"La ville sera entièrement contaminée au jour {jour}")

# contamination()
# contamination_pow()



# def contamination_mondial():
#     nb_habitant = 7800000000  # Nombre total d'habitants
#     nb_malade = 1        # Nombre initial de malades
#     jour = 0             # Compteur de jours

#     while nb_malade < nb_habitant:
#         nb_malade = pow(3, jour)  # Calcul exponentiel : chaque jour, les malades triplent
#         jour += 1

#     print(f"La ville sera entièrement contaminée au jour {jour}")

# contamination_mondial()
import tkinter as tk
from PIL import Image, ImageTk  # Pour afficher des images avec Tkinter
from dictionnaire import dictionnaire


def propagation_maladie(maladie):
    """Calcule le nombre de jours nécessaires pour contaminer toute la population."""
    nb_habitant = 15000  # Nombre total d'habitants
    nb_malade = 1        # Nombre initial de malades
    jour = 0             # Compteur de jours

    while nb_malade < nb_habitant:
        nb_malade = pow(dictionnaire[maladie]["r_0"], jour)
        jour += 1

    return jour


def afficher_resultats():
    """Affiche les informations et le résultat dans l'interface Tkinter."""
    maladie = maladie_var.get()  # Récupère la maladie sélectionnée dans le menu déroulant

    if maladie in dictionnaire:
        # Récupère les informations de la maladie
        infos = dictionnaire[maladie]
        jours_contamination = propagation_maladie(maladie)
        symptomes = ", ".join(infos["symptomes"])

        # Efface le texte précédent et insère les résultats
        text_widget.delete("1.0", tk.END)
        text_widget.insert(
            tk.END,
            f"Maladie : {infos['nom']}\n"
            f"Symptômes : {symptomes}\n"
            f"R₀ (taux de reproduction) : {infos['r_0']}\n"
            f"La ville sera entièrement contaminée en {jours_contamination} jours.\n"
        )

        # Charger et afficher l'image
        image_path = infos.get("image")
        if image_path:
            image = Image.open(image_path)
            image = image.resize((700, 500))  # Redimensionne l'image
            photo = ImageTk.PhotoImage(image)
            image_label.configure(image=photo)
            image_label.image = photo
        else:
            image_label.configure(image=None)
            image_label.image = None
    else:
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, "Erreur : Maladie non trouvée.")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Propagation des Maladies")

# Variable pour le choix de la maladie
maladie_var = tk.StringVar(root)
maladie_var.set("rougeole")  # Maladie sélectionnée par défaut

# Menu déroulant pour choisir la maladie
options = list(dictionnaire.keys())
dropdown = tk.OptionMenu(root, maladie_var, *options)
dropdown.pack(pady=10)

# Bouton pour afficher les résultats
btn_calculer = tk.Button(root, text="Calculer", command=afficher_resultats)
btn_calculer.pack(pady=10)

# Zone de texte pour afficher les résultats
text_widget = tk.Text(root, width=60, height=10)
text_widget.pack(pady=10)

# Zone pour afficher l'image
image_label = tk.Label(root)
image_label.pack(pady=10)

# Lancement de l'application Tkinter
root.mainloop()