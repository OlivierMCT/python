maListe = []
print("maListe", maListe)
print("maListe", type(maListe))

maListe.append(11)
maListe.append("douze")
maListe.append(13.33)
print("maListe", maListe)

maListe2 = list()

loto = [22, 33, 44, 44, 55, 77, 88]
print("loto", loto)

# Ajout de 99 en fin
loto.append(99)
loto += [99]
loto.extend([99])
print("loto", loto)

# Retrait de 99 en fin
loto.pop()
dernier = loto.pop()
print("dernier", dernier)
print("loto", loto)

# Ajout de 11 en debut
loto = [11] + loto
loto.insert(0, 11)
print("loto", loto)

# Retrait de 11 en début
premier = loto.pop(0)
print("premier", premier)
print("loto", loto)

# Insertion de 66 entre 55 et 77
indiceDe77 = loto.index(77)
loto.insert(indiceDe77, 66)
print("loto", loto)

# Suppression de 44
loto.remove(44)
print("loto", loto)


# -------------------------------
# Tous les chemins menent aux listes !

ensemble = range(11, 100, 11)
print("ensemble", ensemble, type(ensemble))

ensemble = list(ensemble)
print("ensemble", ensemble, type(ensemble))

prenom = "Olivier"
print("prenom", prenom, type(prenom))

prenom = list(prenom)
print("prenom", prenom, type(prenom))
prenom[3] = "V"
prenom[-1] = "R"
print("prenom", prenom, type(prenom))

# prenom = str(prenom) #[, , , , ]
prenom = "".join(prenom)
print("prenom", prenom, type(prenom))


# -- Range ---------------------------
loto = list(range(11, 100, 11))
print("loto", loto)
print("premier", loto[0])
print("deuxieme", loto[0 + 1])
print("dernier", loto[-1])

print("les 3 premiers", loto[0:3])
print("les 3 premiers", loto[:3])

print("du 2eme au 5eme", loto[1:5])

print("du 4eme au dernier", loto[3:len(loto)])
print("du 4eme au dernier", loto[3:])

print("du 5eme a l'avant dernier", loto[4:len(loto) - 1])
print("du 5eme a l'avant dernier", loto[4:-1])

print("les 3 derniers", loto[len(loto) - 3:len(loto)])
print("les 3 derniers", loto[-3:len(loto)])
print("les 3 derniers", loto[-3:])

print("tous sauf les 3 derniers", loto[:-3])

print("les elements à un indice impair", loto[1:len(loto):2])
print("les elements à un indice impair", loto[1::2])

print("les elements à un indice pair", loto[0::2])
print("les elements à un indice pair", loto[::2])

print(
  "les 2 derniers à un indice pair", 
  loto[len(loto)-1:len(loto)-4:-2]
)

print("les 2 derniers à un indice pair", loto[-1:-4:-2])
print("les 2 derniers à un indice pair", loto[:-4:-2])

print("reverse", loto[::-1])

copie = loto[:]
print("loto", loto)
print("copie", copie)

copie[0] = 111
print("loto", loto)
print("copie", copie)




