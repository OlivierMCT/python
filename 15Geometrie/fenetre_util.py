from tkinter import Button, Canvas, Label

from figure import *

def creerLabel(fenetre, texte) -> Label:
    return Label(
        fenetre,
        text=texte,
        background="#7C7C7C",
        foreground="#ffffff",
        font=('Courier New', 42)
    )


def creerCanvas(fenetre, width, height) -> Canvas:
    return Canvas(
        fenetre,
        width=width,
        height=height,
        background='#7C7C7C'
    )

def creerButton(fenetre, texte, command) -> Button:
    return Button(
        fenetre,
        text=texte,
        font=('Courier New', 25),
        command=command
    )

def creerRectangle(canvas: Canvas, carre: Carre):
    canvas.create_rectangle(
      carre.centre.x - (carre.cote / 2),
      carre.centre.y - (carre.cote / 2),
      carre.centre.x + (carre.cote / 2),
      carre.centre.y + (carre.cote / 2),
      fill=carre.couleur,
      outline=carre.couleur
    )

def creerOval(canvas: Canvas, cercle: Cercle):
    canvas.create_oval(
      cercle.centre.x - (cercle.rayon),
      cercle.centre.y - (cercle.rayon),
      cercle.centre.x + (cercle.rayon),
      cercle.centre.y + (cercle.rayon),
      fill=cercle.couleur,
      outline=cercle.couleur
    )