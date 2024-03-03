nb = 22

if(nb > 20):
    print("oui !")
    print(nb, "est supérieur à 20")

if(nb < 10):
    print(nb, "est inférieur à 10")
else:
    print(nb, "est supérieur ou égal à 10")

if(nb < 10):
    print(nb, "est inférieur à 10")
elif(nb < 20):
    print(nb, "est supérieur ou égal à 10 ET inférieur à 20")
else:
    print(nb, "est supérieur ou égal à 20")

if nb == 20:
    pass
print("suite")

i = 0
while (i < 10):
    print('Itération n°', i)
    i += 1

# foreach
ensemble = range(10, 20)  # [10, 20[
for element in ensemble:
    print('element =', element)
print("-----------------")
for element in range(10, 20, 3):
    print('element =', element)
print("-----------------")
for element in range(10, 0, -1):
    print('element =', element)

print("-----------------")
for seconde in range(10, -1, -1):
    if(seconde == 6):
        continue

    if(seconde == 3):
        print("annulation 🙊")
        break

    if(seconde != 0):
        print(seconde)
    else:
        print("décollage 🚀")

prenom = "Olivier"
for lettre in prenom:
    print(lettre)


motDePasse = "azertyUiOp"
mdpSecure = "" # motDePasse avec des * à la place des voyelles

voyelles = "aeiouyAEIOUY"
for lettre in motDePasse:
  mdpSecure += "*" if(lettre in voyelles) else lettre
print("🔒", mdpSecure)

for elt in range(0, 10):
  print(elt)
  if(elt == 5):
    break
else:
  print("What else !")
