import json 

with open('data.json', "r") as f:
    donnees = json.load(f)

donnees["age"] = 25

with open('data.json', "w") as f:
    json.dump(donnees, f, indent=4)


# erreur courante
# r = read = lire dans le fichier
# w = write = écrire dans le fichier
# a = append = ajouter à la fin du fichier
# x = exclusive = créer un nouveau fichier, échoue si le fichier existe déjà
# t = text = texte
# b = binary = binaire



# fermer le fichier
# f.close()




#  erreur fichier json

