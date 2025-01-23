import CompteBancaire as compte

# Création d'une instance avec l'alias
c = compte.CompteBancaire()

# Vérification des attributs et méthodes
print(c)
print(dir(c))

# Création et manipulation des comptes
compte1 = compte.CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

compte2 = compte.CompteBancaire()
compte2.depot(25)
compte2.affiche()


