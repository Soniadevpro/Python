import string


class Alphabet_majuscule(object):
    """Classe mère"""
    def __init__(self):
        self.lettres_maj = string.ascii_uppercase
        # équivalent à une chaîne reprenant tout l'alphabet avec la méthode upper()

# class Alphabet_majuscule(object): vous construisez votre classe mère comme une classe normale et ordinaire
#self.lettres = string.ascii_uppercase importation de la constante "string.ascii_uppercase" du module "string" qui est l'alphabet


class Alphabet_minuscule(Alphabet_majuscule):
    """Classe fille"""
    def __init__(self):
        Alphabet_majuscule.__init__(self)
        self.lettres_min = self.lettres_maj.lower()


#class Alphabet_minuscule(Alphabet_majuscule): en paramètre de la classe fille, le nom de la classe mère.
#Alphabet_majuscule.__init__(self) dans le constructeur de la classe fille, importation du constructeur de la classe mère avec ses attributs

test = Alphabet_majuscule()
print(test.lettres_maj)

test2 = Alphabet_minuscule ()

print(test2.lettres_min)

print(test2.lettres_maj)