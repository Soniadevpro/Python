class Compte:
    """Un exemple de classe"""
    
    def __init__(self, solde_initial):
        """Initialisation de l'attribut d'instance solde"""
        self.solde = float(solde_initial)

    def nouveau_solde(self, somme):
        """Nouveau solde de compte avec la valeur somme"""
        self.solde = float(somme)

    def solde(self):
        """Retourne le solde"""
        return self.solde

    def credit(self, somme):
        """Crédite le compte de la valeur somme. Retourne le solde"""
        self.solde += somme
        return self.solde

    def debit(self, somme):
        """Débite le compte de la valeur somme. Retourne le solde"""
        self.solde -= somme
        return self.solde

    def __add__(self, somme):
        """x.__add__(somme) <=> x + somme
        Crédite le compte de la valeur de la somme
        Affiche 'Nouveau solde : somme'"""
        self.solde += somme
        print(f"Nouveau solde : {self.solde}")
        return self

    def __sub__(self, somme):
        """x.__sub__(somme) <=> x-somme
        Débite le compte de la valeur de la somme
        Affiche 'Nouveau solde'"""
        self.solde -= somme
        print(f"Nouveau solde : {self.solde}")
        return self
#----------------------------------------------------------------------------------



if __name__=='__main__':
    """Bloc d'instruction programme principal"""
    cb1 = Compte(1000)

    print(f"{cb1.Solde()}")
    print(f"{cb1.Credit()}")
    print(f"{cb1.Debit()}")
    print(f"{cb1.Solde()}")
        
    cb1.Nouveau_solde(5100)
    print(f"{cb1.Solde}")
    cb1 + 253.2
    cb1 - 1000 + 100


