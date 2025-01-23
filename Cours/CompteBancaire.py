
class CompteBancaire:
    def __init__(self, nom="Dupont", solde=1000):
        """Création ou initialisation ou constructeur de la classe"""
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        """Ajout d'une somme à l'attribut solde"""
        self.solde += somme

    def retrait(self, somme):
        """Retrait d'une somme à l'attribut solde"""
        self.solde -= somme

    def affiche(self):
        """Affichage des informations"""
        print(f"Titulaire: {self.nom}, Solde: {self.solde:.2f}€")