# Mon commentaire

# Types de données
entier = 5
print("entier =", entier, type(entier))

entier = 5.9
print("entier =", entier, type(entier))

oui = True
non = False
print("oui =", oui, type(oui))
print("non =", non, type(non))

prenom = "Olivier"
print("prenom =", prenom, type(prenom))
nom = 'Astre'
print("nom =", nom, type(nom))
test1 = "dedans [']"
test2 = 'dedans ["]'
test3 = 'dedans [\']'
test4 = "dedans [\"]"
print("test1 =", test1, type(test1))
print("test2 =", test2, type(test2))
print("test3 =", test3, type(test3))
print("test4 =", test4, type(test4))
test5 = "dedans [\t]"
print("test5 =", test5, type(test5))

citation = """ "Aujourd'hui il fait beau !" 
(météo france) """
print("citation =", citation, type(citation))

# Opérateurs
nb1 = 45
nb2 = 16
somme = nb1 + nb2
print(nb1, "+", nb2, "=", somme)
print(nb1, "-", nb2, "=", nb1 - nb2)
print(nb1, "*", nb2, "=", nb1 * nb2)
print(nb1, "/", nb2, "=", nb1 / nb2)
print(nb1, "/", nb2, "=", nb1 // nb2)
print(nb1, "modulo", nb2, "=", nb1 % nb2)
print(nb1, "puissance", nb2, "=", nb1 ** nb2)

nomComplet = prenom + " " + nom
print("nomComplet =", nomComplet)

# operation = nb1 + " + " + nb2 + " = " + somme
# print(operation)

print(nb1, "identique à", nb2, "?", nb1 == nb2)
print(nb1, "différent de", nb2, "?", nb1 != nb2)
print(nb1, "inférieur à", nb2, "?", nb1 < nb2)
print(nb1, "inférieur ou égal à", nb2, "?", nb1 <= nb2)
print(nb1, "superieur à", nb2, "?", nb1 > nb2)
print(nb1, "superieur ou égal à", nb2, "?", nb1 >= nb2)

print(nb1 < 20 and nb2 > 30)
print(nb1 < 20 or nb2 > 30)
print(not nb1 < 20)