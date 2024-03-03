# RegEx: template pour rechercher ou valider une chaine

# . n'importe quoi
# [abc] a ou b ou c

# [0123456789] un chiffre
# [0-9] un chiffre
# \d un chiffre
# [^0-9] tout sauf un chiffre
# \D tout sauf un chiffre

# [a-z] une lettre en minuscule
# [A-Z] une lettre en majuscule
# [A-DF-Z] une lettre en majuscule sauf E
# [A-Za-z] une lettre en majuscule ou en minuscule

# [a-zA-Z0-9_]  \w 
# [^a-zA-Z0-9_]  \W 

# \s les espaces [  ]
# \S

# * [0, inifini]
# + [1, inifini]
# ? [0, 1]
# {5, 13} entre 5 et 13 inclu
# {16,} au moins 16
# {6} 6

# | ou

# (([a-z][0-9])|([0-9][a-z])){5, 10}

# ([a-z]\.?[0-9]){5}
# ([a-z][.]?[0-9]){5}

# [ab]{16,}\?[cde]{1, 5}

# (\W|\S)*

import re
pattern = r"[Oo].*ivi.*"
chaine = "Olivier"
print( re.match(pattern, chaine) )

pattern = r"^((0[1-9][0-9]{3})|([1-8][0-9]{4})|(9[0-8][0-9]{3}))$"

goodCP = ["33000", "01000", "98999", "73000", "22140"]
badCP = ["00000", "99999", "00", "0", "2A444", "923456", "123456"]

[print(re.match(pattern, cp)) for cp in goodCP]
[print(re.match(pattern, cp)) for cp in badCP]

data = "mon_nom=Astre;mon_prenom=Olivier;mon_email=olivier.astre@outlook.fr"
pattern = r"mon_nom=(?P<nom>[A-Z]( ?[a-zA-Z])*);mon_prenom=(?P<prenom>[A-Z]( ?[a-zA-Z])*);mon_email=(?P<email>.*)"

match = re.match(pattern, data)
print(match)
print(match[0])
print(match[1])
print(match[2])
print(match[3])
print(match[4])
print("Bonjour", match["prenom"], match["nom"], "!")

