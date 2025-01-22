# try catch
# exemple avec try catch

# dans quel cas utiliser try catch ?
# - lorsqu'on sait qu'une erreur peut se produire
# - lorsqu'on veut gérer l'erreur
# - lorsqu'on veut éviter que le programme s'arrête

# exemple

import random

try:
    print("Entrez un nombre")
    a = int(input())
    print("Entrez un autre nombre")
    b = int(input())
    print("Le résultat de la division est", a/b)
except ZeroDivisionError:
    print("Division par zéro")

def juste_prix():
    prix_hasard = random.randint(0, 100)
    
    while True:
        try:
            prix_choisi = int(input("Devinez le prix (entre 0 et 100) : "))
            
            if prix_choisi == prix_hasard:
                print("Bravo ! Vous avez trouvé le juste prix !")
                break
            
            message = "C'est moins !" if prix_choisi > prix_hasard else "C'est plus !"
            print(message)
            
        except ValueError:
            print("Veuillez entrer un nombre valide !")

if __name__ == "__main__":
    juste_prix()