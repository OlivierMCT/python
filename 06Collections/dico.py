monDico1 = {
  "mars": 31,
  "décembre": 31
}
monDico1["janvier"] = 31

print("décembre =>", monDico1["décembre"] , "jours")
monDico2 = dict()

stock = {
  "ordinateur": 12,
  "c/s": [13, 21],
  "ecran": {
    "21p": 2,
    "24p": 14,
    "27p": 6,
    "32p": 3
  }
}
print("stock", stock)
#-------------------------------------
stock = dict()
stock["ordinateur"] = 12

stock["c/s"] = list()
stock["c/s"].append(13)
stock["c/s"].append(21)

stock["ecran"] = dict()
stock["ecran"]["21p"] = 2
stock["ecran"]["24p"] = 14
stock["ecran"]["27p"] = 6
stock["ecran"]["32p"] = 3

print("stock", stock)


print("Nombre d'ordinateurs =", stock["ordinateur"])
print("Nombre de souris =", stock["c/s"][-1])
print("Nombre de 32p =", stock["ecran"]["32p"])
print("Nombre de categories =", len(stock))

dicoEcrans = stock["ecran"]
valeursEcran = dicoEcrans.values()
print(valeursEcran, type(valeursEcran))
listeValeurEcran = list(valeursEcran)
totalEcran = 0
for v in listeValeurEcran:
  totalEcran += v
print(totalEcran, "écrans en stock")

totalEcran = 0
for v in list(stock["ecran"].values()):
  totalEcran += v
print(totalEcran, "écrans en stock")

print(sum(list(stock["ecran"].values())), "écrans en stock")

calendrier = {
  "janvier": 31, "février": 28, "mars": 31,
  "avril": 30, "mai": 31, "juin": 30,
  "juillet": 31, "aout": 31, "septembre": 30,
  "octobre": 31, "novembre": 30, "décembre": 31,
}

print("-- Clés -----------")
cles = list(calendrier.keys())
cles.sort()
for k in cles:
  print(k)

print("-- Valeurs -----------")
valeurs = list(calendrier.values())
valeurs.sort()
for v in valeurs:
  print(v)

print("-- Pairs -----------")
pairs = list(calendrier.items())
for item in pairs:
  print(item, "cle =", item[0], "valeur =", item[1])

for item in pairs:
  c, v = item
  print(item, "cle =", c, "valeur =", v)

for (clef, valeur) in pairs:
  print("cle =", clef, "valeur =", valeur)