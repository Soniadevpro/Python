# for in 
import requests
if __name__ == "__main__":
    result = requests.get("https://www.google.com")
    print(result.content)

for i in [ 88, 1, 8, 5, 14 ]:
    print(i)


for letter in "hello":
        print(letter)

for i in range(10):
    print("hello")


# boucle while


i = 0
while i < 10:
    print("bonjour")
    i += 1


continuer = "o"
while continuer == "o":
    print("on continue...")
    continuer = input("voulez vous continuer ? o/n : ")


# break et continue

liste = [ "1", "2", "3", "4", "Paul", "6", "Pierre" ]
for element in liste:
    if element.isalpha():
        break
    print(element)



# boucle for else


prenoms = [ "Paul", "Pierre", "Jacques" ]
for prenom in prenoms:
    if prenom == "Jean-Jacques":
        print("Jean est dans la liste")
        break
else:
    print("Jean n'est pas dans la liste")




# comprehension de liste



liste = [ -1, -2, 3, 4, 5 ]
liste_nb_positifs = [ i * 2 for i in liste if i > 0 ]

print(liste_nb_positifs)


# Les fonctions any() et all() permettent de vérifier si au moins un élément d'une liste est vrai ou si tous les éléments d'une liste sont vrais.


notes = [ 10, 12, 15, 8, 14 ]
print(all([ note >= 10 for note in notes ]))
print(any([ note >= 10 for note in notes ]))


a = 35
b = 25

def addition(a, b):
    return a + b

print(addition(a, b))