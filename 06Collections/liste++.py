from functools import reduce


loto = [33, 11, 99, 44, 66, 77, 55, 22, 88]
print("loto", loto)
loto.sort()
print("loto", loto)

def estImpair(nombre: int) -> bool:
  return nombre % 2 != 0

lotoImpairs = []
for nb in loto:
  if estImpair(nb):
    lotoImpairs.append(nb)
print("lotoImpairs", lotoImpairs)

lotoImpairs = list(filter(estImpair, loto))
print("lotoImpairs", lotoImpairs)

lotoImpairs = list(filter(lambda nombre: nombre % 2 != 0, loto))
print("lotoImpairs", lotoImpairs)

lotoImpairs = [nb for nb in loto if nb % 2 != 0]
print("lotoImpairs", lotoImpairs)

lotoFoisOnze = [nb * 11 for nb in loto]
print("lotoFoisOnze", lotoFoisOnze)

lotoFoisOnze = list(map(lambda nb: nb * 11, loto))
print("lotoFoisOnze", lotoFoisOnze)

produit = reduce(lambda precedent, actuel: precedent * actuel, loto)

print(" x ".join(map(lambda nb: str(nb), loto)), "=", produit)


prenoms = ["doNalD", "    ", "  MiCKey   ", "miNNiE", "", "DAIsY   ", "  Balthazar"]
print(prenoms)

prenoms = map(lambda s: s.strip(), prenoms)
prenoms = map(lambda s: s.capitalize(), prenoms)
prenoms = filter(lambda s: s != '', prenoms)
#prenoms = list(filter(lambda s: len(s) != 0, prenoms))
print(list(prenoms))

prenoms = ["doNalD", "    ", "  MiCKey   ", "miNNiE", "", "DAIsY   ", "  Balthazar"]
prenoms = filter(lambda s: s != '', map(lambda s: s.capitalize(), map(lambda s: s.strip(), prenoms)))
print(list(prenoms))

prenoms = ["doNalD", "    ", "  MiCKey   ", "miNNiE", "", "DAIsY   ", "  Balthazar"]
prenoms = filter(lambda s: s != '', map(lambda s: s.strip().capitalize(), prenoms))
print(list(prenoms))

prenoms = ["doNalD", "    ", "  MiCKey   ", "miNNiE", "", "DAIsY   ", "  Balthazar"]
prenoms = [s.strip().capitalize() for s in prenoms if s.strip() != '']
print(list(prenoms))

prenoms = ["doNalD", "    ", "  MiCKey   ", "miNNiE", "", "DAIsY   ", "  Balthazar"]
prenoms = [s.capitalize() for s in [s2.strip() for s2 in prenoms] if s != '']
prenoms.sort()
print(list(prenoms))

#list(map(lambda p: print("Bonjour", p, "!"), prenoms))
[print("Bonjour", p, "!") for p in prenoms]