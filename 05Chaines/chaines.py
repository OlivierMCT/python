nom = "alain oliVieR aStRE du chateau"  # en lecture seule

print(nom, "contient", len(nom), "caractères")
print("premier caractère:", nom[0])
print("deuxième caractère:", nom[0 + 1])
print("dernier caractère:", nom[len(nom) - 1])
print("dernier caractère:", nom[-1])
print("avant dernier caractère:", nom[-2])
#nom[0] = "T"
print("MAJ:", nom.upper())
print("Brut:", nom)
print("min:", nom.lower())
print("title:", nom.title())
print("capi:", nom.capitalize())

mots = nom.split(" ")
print("Découpage en", len(mots), "mots")
print("premier mot", mots[0])
print("deuxieme mot", mots[1])
print("dernier mot", mots[-1])
print("derniere lettre du premier mot", mots[0][-1])

email = (mots[0] + "." + mots[1] + "@disney.com").lower()
print(email)
email = (".pro.".join(mots) + "@disney.com").lower()
print(email)

nb = 101
message = "numero du jour: " + str(nb)
print(message)
