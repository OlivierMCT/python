from fraction_class import fraction
from fractionerror_class import fractionError


def afficherFraction(f: fraction, nom: str) -> None:
    template = "{0} = {1} = {2:.4f}"
    print(template.format(nom, f.transformerEnChaine(), f.calculerQuotient()))


# instanciation d'une fraction
f1 = fraction(12, 29)
afficherFraction(f1, "f1")

f2 = fraction(4)
afficherFraction(f2, "f2")

f3 = fraction(224682, 6642822)
afficherFraction(f3, "f3")
# 22/12 = 11/6
f3.reduire()
afficherFraction(f3, "f3")

try:
    f3.denominateur = 0
    print("Den =", f3.denominateur)
except:
    print('Oooops :/')

try:    
    f4 = fraction(5, 0)
    print("Den =", f4.denominateur)
except fractionError as err:
    print('Oooops :/', err.numero, err)
except :
    print('Oooops :/')

print("-------------------------")
fUn = fraction(2, 7)
fDeux = fraction(5, 9)

print(fUn, "+", str(fDeux))
print(fUn, "+", fDeux, "=", (fUn + fDeux))
print(fUn, "+", fDeux, "=", (fUn / fDeux))