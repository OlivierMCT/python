from xml.dom.minidom import Node, parse
from figure import *

def transformerElementEnFigure(elt) -> Figure:
  if(elt.nodeName == "carre"):
    return transformerElementEnCarre(elt)
  if(elt.nodeName == "cercle"):
    return transformerElementEnCercle(elt)
  raise ValueError("ni un cercle, ni un carré")

def transformerElementEnCarre(elt) -> Carre:
  c = Carre()
  c.couleur = elt.getAttribute("couleur")
  c.cote = int(elt.getElementsByTagName("cote")[0].firstChild.nodeValue)
  c.centre = transformerElementEnCoordonnee(elt.getElementsByTagName("centre")[0])
  return c

def transformerElementEnCercle(elt) -> Cercle:
  c = Cercle()
  c.couleur = elt.getAttribute("couleur")
  c.rayon = int(elt.getElementsByTagName("rayon")[0].firstChild.nodeValue)
  c.centre = transformerElementEnCoordonnee(elt.getElementsByTagName("centre")[0])
  return c

def transformerElementEnCoordonnee(elt) -> Coordonnee:
  point = Coordonnee()
  point.x = int(elt.getElementsByTagName("x")[0].firstChild.nodeValue)
  point.y = int(elt.getElementsByTagName("y")[0].firstChild.nodeValue)
  return point

document = parse("figures.xml")
racine = document.documentElement
figures = [transformerElementEnFigure(n) for n in racine.childNodes if n.nodeType == Node.ELEMENT_NODE]
[print(f) for f in figures]