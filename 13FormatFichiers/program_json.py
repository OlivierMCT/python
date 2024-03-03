import json
from figure import *

def obtenirCarreFromJson(data) -> Carre:
  c = Carre()
  c.couleur = data["couleur"]
  c.cote = data["cote"]
  centre = Coordonnee()
  centre.x = data["centre"]["x"]
  centre.y = data["centre"]["y"]
  c.centre = centre
  return c

def obtenirCercleFromJson(data) -> Cercle:
  c = Cercle()
  c.couleur = data["couleur"]
  c.rayon = data["rayon"]
  centre = Coordonnee()
  centre.x = data["centre"]["x"]
  centre.y = data["centre"]["y"]
  c.centre = centre
  return c

with open("figures.json", "r") as flux:
  data = json.loads(flux.read())

[print(obtenirCarreFromJson(c)) for c in data["carres"]]
[print(obtenirCercleFromJson(c)) for c in data["cercles"]]