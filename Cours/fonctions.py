# Les fonctions prédéfinies
# Nous avons déjà utilisé quelques fonctions sans le savoir :
#  print () : affiche n’importe quel nombre de valeurs passées en arguments.
#  input () : interrompt le programme jusqu’à ce que l’utilisateur entre une chaîne de caractères puis
# presse la touche « Entrée ». Alors, le programme redémarre et affiche la chaîne de caractères.
#  int () : transforme une chaîne de caractères en nombre entier (si celle-ci s’y prête) ou un nombre
# décimal en nombre entier (en ignorant ce qui est après la virgule).
#  float () : transforme une chaîne de caractères en nombre décimal (si celle-ci s’y prête) ou un
# nombre entier en nombre décimal (exemple : 9.0)
#  str () : transforme un nombre entier ou un nombre décimal en chaîne de caractères.


def ma_fonction():
  
    return

# La fonction ci-dessus ne fait rien, elle ne renvoie rien. Elle est vide. Elle ne fait que définir une fonction.

def fonction_affichage():
    print("Bonjour")
    return 

fonction_affichage()

# fonction qui divise par deux 

def diviser_par_deux(nombre):
    resultat = nombre / 2
    return resultat

print(diviser_par_deux(10))


# fonction qui multiplie par deux

def multiplier_par_deux(nombre):
    resultat = nombre * 2
    return resultat

print(multiplier_par_deux(10))


#fonction avec 2 paramètres

def additionner_deux_nombres(nombre1, nombre2):
    resultat = nombre1 + nombre2
    return resultat

print(additionner_deux_nombres(10, 20))

# À quoi sert la docstring?
# La docstring est une chaîne de caractères indentée juste après la déclaration d’une fonction. Elle
# fournit une documentation accessible grâce à la fonction help () :

def additionner_deux_nombres(nombre1, nombre2):
    """
    Cette fonction additionne deux nombres.
    """
    resultat = nombre1 + nombre2
    return resultat

help(additionner_deux_nombres)



# paramètres par défaut

def additionner_deux_nombres(nombre1, nombre2=0):
 
    resultat = nombre1 + nombre2
    return resultat

print(additionner_deux_nombres(10))

#nombre d'argument indéterminé

def additionner_nombres(*nombres):
    resultat = 0
    for nombre in nombres:
        resultat += nombre
    return resultat

print(additionner_nombres(10, 20, 30, 40, 50))

# Les Fonctions powerful

# MAP
# Le map est une fonction intégrée par les programmeurs afin de rendre le programme plus efficient, cette
# fonction itère sur tous les éléments spécifiés sans l’utilisation de boucles.


def carre(x):
    multiplication = x * x
    return multiplication

liste = [1, 2, 3, 4, 5]
resultat = map(carre, liste)
print(list(resultat))


# FILTER
# Le filter est une fonction intégrée qui est utilisée quand il faut séparer un grand nombre de données.
# Il est utilisé pour extraire les données en fonction de la condition.


def est_positif(x):
    return x > 0

liste = [-1, 2, -3, 4, -5]
resultat = filter(est_positif, liste)
print(list(resultat))


# LAMBDA
# Il est dit « anonyme » car on peut instancier et déclarer une fonction sans nom. Si vous avez une seule
# opération à exécuter, le lambda est extrêmement utile au lieu de déclarer une fonction traditionnelle.
# Lambda est similaire à la fonction, sauf qu'il ne peut renvoyer qu'une seule expression.

liste = [1, 2, 3, 4, 5]
resultat = map(lambda x: x * x, liste)
print(list(resultat))


# REDUCE
# Cette fonction est utilisée quand il est nécessaire d'appliquer le même opérateur à la même opération à
# tous les éléments de la liste donnée. « reduce » fait partie de la méthode functools.


from functools import reduce

def additionner(x, y):
    return x + y

liste = [1, 2, 3, 4, 5]
resultat = reduce(additionner, liste)
print(resultat)

# Le zip est une fonction intégrée qui est utilisée pour extraire des données de différentes colonnes de
# la base de données et les transformer en tuple.

liste1 = [1, 2, 3, 4, 5]
liste2 = ['a', 'b', 'c', 'd', 'e']
resultat = zip(liste1, liste2)
print(list(resultat))


def add_liste (a, b):
        
    return a + b

sortie = list(map(add_liste, [1, 2, 3], [4, 5, 6]))
print("sortie", sortie)


def est_positif(x):
    return x > 0
sortie = list(filter(est_positif, [-1, 2, -3, 4, -5]))

print("sortie", sortie)

variable = lambda a, b : a**2 + b**2 + 2* (a*b)
print(variable(4, 5))


