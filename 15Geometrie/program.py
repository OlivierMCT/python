import json
import tkinter
from tkinter import filedialog
from fenetre_util import *
from figure import *

def creerCarre(data) -> Carre:
    x = data["centre"]["x"]
    y = data["centre"]["y"]
    return Carre(x, y, data["cote"], data["couleur"])


def creerCercle(data) -> Cercle:
    x = data["centre"]["x"]
    y = data["centre"]["y"]
    return Cercle(x, y, data["rayon"], data["couleur"])


def chargerFigures():
    nomFichier = filedialog.askopenfilename(
        title="Fichier Figures",
        filetypes=[("Fichiers JSON", "*.json")],
        initialdir="."
    )
    fenetre.title('Géométrie | ' + nomFichier)
    with open(nomFichier, "r") as flux:
        allData = json.loads(flux.read())
    [creerOval(dessinCanvas, creerCercle(c)) for c in allData["cercles"]]
    [creerRectangle(dessinCanvas, creerCarre(c)) for c in allData["carres"]]


fenetre = tkinter.Tk()
fenetre.title('Géométrie')
fenetre.resizable = False

titreLabel = creerLabel(fenetre, "Géométrie")
titreLabel.pack()

fichierButton = creerButton(fenetre, "Choisir Fichier", chargerFigures)
fichierButton.pack()

dessinCanvas = creerCanvas(fenetre, 1200, 800)
dessinCanvas.pack()

fenetre.mainloop()
