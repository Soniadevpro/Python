import os

chemin = "C:/Users/sonia/Desktop/Python/"

with open(chemin + "fichier.txt", "a") as fichier:
    contenu = fichier.write("\nbienvenue dans le fichier")
    print(contenu)