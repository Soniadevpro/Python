# Calculatrice simple
premierNombre = input(" Veuillez entrer un premier nombre : ")
deuxiemeNombre = input(" Veuillez entrer un deuxième nombre : ")
operateur = input(" Veuillez entrer un opérateur : ")

if operateur == "+":
    resultat = int(premierNombre) + int(deuxiemeNombre)
elif operateur == "-":
    resultat = int(premierNombre) - int(deuxiemeNombre)
elif operateur == "*":
    resultat = int(premierNombre) * int(deuxiemeNombre)
elif operateur == "/":
    resultat = int(premierNombre) / int(deuxiemeNombre)
else:
    resultat = "Erreur"


print("Le résultat est : ", resultat)