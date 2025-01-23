# appel du module

import Personne as pers

p = pers.Personne() # instancier l'objet
print(p)
print(dir(p))



liste = []

n = int(input("Nb de pers : "))

for i in range(0, n):
    a = pers.Personne()
    a.saisie()
    liste.append(a)

for p in liste:
    print("------")
    p.affichage()

    



p.saisie()
p.retraite(40)
