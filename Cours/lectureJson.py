import json

chemin = "C:/Users/sonia/Desktop/Python/fichier.json"

with open(chemin, "r") as f:

    liste = json.load(f)
    print(type(liste))
    # json.dump(list(range(25)), f, indent=4)