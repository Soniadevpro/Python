import os

chemin = "C:/Users/sonia/Desktop/Python/"
fichier = chemin + "MotReserve.txt"

print(f"Chemin complet du fichier : {fichier}")

# Vérifier si le fichier existe
if os.path.exists(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
        print("Contenu du fichier :")
        print(contenu)
else:
    print(f"Erreur : le fichier '{fichier}' n'existe pas.")


