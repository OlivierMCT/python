import json
from figure import *

tableau = ["coucou", 10, True]
with open("data1.json", "w") as flux:
    flux.write(json.dumps(tableau, indent=2))

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
with open("data2.json", "w") as flux:
    flux.write(json.dumps(stock, indent=2))

c = Cercle()
c.centre = Coordonnee()
c.centre.x = 11
c.centre.y = 22
c.rayon = 33
c.couleur = "cyan"
#c.centre = None
with open("data3.json", "w") as flux:
    flux.write(json.dumps(c.__dict__, indent=2))
