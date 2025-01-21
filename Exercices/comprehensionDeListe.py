# compréhension de liste en python page 47
# fonction avec boucle 
# def liste_initiale():
#     liste_init = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#     liste_2 = []

#     for i in liste_init:
#         liste_2.append(i*2)
#     print(liste_2)

# liste_initiale()

# fonction avec compréhension de liste
# def liste_initiale():
#     liste_init = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#     liste_2 = [i**2 for i in liste_init]
#     print(liste_2)

# liste_initiale()
   # def avec range

# def liste_range ():
#     liste_2 = [i**2 for i in range(16)]
#     print(liste_2)

# liste_range()


#version sans compréhension de liste

# liste_init = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# liste_pair = []

# for i in liste_init:
#     if i % 2 == 0:
#         liste_pair.append(i)

# print(liste_pair)




# version avec compréhension de liste
# liste_init = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# liste_pair = [i*2 for i in liste_init if i % 2 == 0]

# print(liste_pair)



# liste_init2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# nouvelle_liste = []
# for i in liste_init2:
#     if i % 2 == 0:
#         nouvelle_liste.append(i*2)
#     else:
#         nouvelle_liste.append(i*3)


#         print(nouvelle_liste)

# liste_init3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# nouvelle_liste2 = [i*2 if i % 2 == 0 else i*3 for i in liste_init3]

# print(nouvelle_liste2)


# compréhension de liste avec une liste de listes

liste_de_listes3 = [[0, "a"], [1, "b"], [2, "c"], [3, "d"]]
nouvelle_liste3 = []
for i in liste_de_listes3:
   
    for n in i:
        nouvelle_liste3.append(n*2)

print(nouvelle_liste3)


liste_de_listes = [[0, "a"], [1, "b"], [2, "c"], [3, "d"]]

nouvelle_liste4 = [n*2 for i in liste_de_listes for n in i]

print(nouvelle_liste4)

# liste aleatoire borné en comprehension 

# import random

# liste_aleatoire = [random.randint(0, 100) for i in range(10)]
# print(liste_aleatoire)




# compréhension de liste avec les autres types itérables

prenom = "Jean"

liste_lettres = [lettre for lettre in prenom]
print(liste_lettres)

# Conclusion
# La compréhension de liste est une méthode puissante qui a remplacé les anciennes fonctions map
# () et filter () dont l’usage est aujourd’hui déconseillé. Bien utilisée, la compréhension de liste rend
# le code plus concis, plus élégant et plus facile à comprendre qu’avec les fonctions map () et filter
# (). Il existe une page consacrée aux compréhensions de liste dans la documentation officielle du
# langage Python.

