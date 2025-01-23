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


class Alphabet_tri(Alphabet_minuscule):
    # classe petite fille
    def __init__(self):
        Alphabet_minuscule.__init__(self)
        self.voyelles = []
        self.consonnes = []
        for lettre in self.lettres:
            if lettre in "aeiouy":
                self.voyelles.append(lettre)
            else:
                self.consonnes.append(lettre)
    
    def listes_vers_chaine(self):
        self.voyelles_chaine = "".join(self.voyelles) 
        self.consonnes_chaine = "".join(self.consonnes)

test3 = Alphabet_tri()
print(test3.lettres) 
print(test3.voyelles)
print(test3.consonnes)

test3.listes_vers_chaine()
print(test3.voyelles_chaine)
test3.consonnes_chaine()
print(test3.consonnes_chaine)
