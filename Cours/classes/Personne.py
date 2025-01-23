# LES CLASSES
# Une classe est un type permettant de regrouper dans la même structure : les informations
# (champs, propriétés, attributs) relatives à une entité ; les procédures et fonctions permettant de
# les manipuler (méthodes). Champs et méthodes constituent les membres de la classe.
# Remarques :
# • La classe est un type structuré qui va plus loin que l’enregistrement (ce dernier n’intègre que
# les champs).
# • Les champs d’une classe peuvent être de type quelconque. Ils peuvent faire référence à
# d’instances d’autres classes.


# Synthaxe d'une classe

# début définition 

class Personne :

    """ Classe personne  """
    compteur = 0
    #constrcuteur
    def __init__(self):
        #lister les champs
        self.nom = ""
        self.age = 0
        self.salaire = 0.0
        self.id = Personne.compteur

        Personne.compteur += 1
        # fin constructeur

    def saisie(self):
        self.nom = input("Nom: ")
        self.age = int(input("Age: "))
        self.salaire = float(input("Salaire: "))

        print(f"{self.nom} a {self.age} ans et dispose de {self.salaire}€ sur son compte")
#fin saisie

    def retraite (self, limite):
        """Méthode retraite"""
        reste = limite - self.age
        if (reste < 0):
            print("Vous êtes à la retraite")
        else:
            print(f"Il vous reste {reste} années")

    def affichage(self):

        """Méthode d'affichage"""
        print(f"{self.id}")
        print(f"Votre nom {self.nom}")
        print(f"Votre âge {self.age}")
        print(f"Votre salaire {self.salaire}")















#fin définition

