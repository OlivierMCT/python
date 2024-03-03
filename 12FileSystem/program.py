import csv
import glob
import os
import pickle
from personnage import Personnage


def scanDirectory():
    chemin = input("[path]> ")
    if(chemin[-2:] != "\\*"):
        chemin += "\\*"

    listeCompleteAbsolue = glob.glob(chemin)

    dossiers = []
    fichiers = []

    for item in listeCompleteAbsolue:
        if(os.path.isfile(item)):
            fichiers.append(item.split("\\")[-1])
        elif(os.path.isdir(item)):
            dossiers.append(item.split("\\")[-1])

    # for item in listeCompleteAbsolue:
    #   (fichiers if(os.path.isfile(item)) else dossiers).append(item.split("\\")[-1])

    # [(fichiers if(os.path.isfile(item)) else dossiers).append(item.split("\\")[-1]) for item in listeCompleteAbsolue]

    [print("{0:<5} {1:^40}".format("DIR", d)) for d in dossiers]
    [print("{0:<5} {1:^40}".format("FILE", f)) for f in fichiers]


def afficherTousLesPersonnages(persos: list):
    [print(p) for p in persos]


def ecrireDansUnFichierTexte(persos: list):
    with open("persos.txt", "w") as flux:
        [print(p, file=flux) for p in persos]
    # flux.close()


def lireDepuisUnFichierTexte() -> list:
    with open("persos.txt", "r") as flux:
        return [l[:-1] if (l[-1] == "\n") else l for l in flux.readlines()]


def ecrireDansUnFichierCSV(persos: list):
    with open("persos.csv", "w", encoding="UTF-8") as flux:
        writer = csv.writer(flux, dialect=csv.unix_dialect)
        writer.writerow(["Prénom", "Nom", "Animal"])
        writer.writerows([[p.prenom, p.nom, p.animal] for p in persos])
    # flux.close()


def lireDepuisUnFichierCSV() -> list:
    with open("persos.csv", "r", encoding="UTF-8") as flux:
        reader = csv.reader(flux, dialect=csv.unix_dialect)
        return [Personnage(ligne[0], ligne[1], ligne[2]) for ligne in list(reader)[1:]]
    # flux.close()


def lireDepuisUnFichierCSVBis() -> list:
    with open("persos.csv", "r", encoding="UTF-8") as flux:
        reader = csv.DictReader(flux, dialect=csv.unix_dialect)
        return [Personnage(ligne["Prénom"], ligne["Nom"], ligne["Animal"]) for ligne in list(reader)]
    # flux.close()


def ecrireListeDansUnFichierObjet(persos: list):
    with open("persos.pims", "wb") as flux:
        pickle.dump(persos, flux)
    # flux.close()


def ecrireObjetsDansUnFichierObjet(persos: list):
    with open("persos-bis.pims", "wb") as flux:
        [pickle.dump(p, flux) for p in persos]
    # flux.close()


def lireListeDepuisUnFichierObjet() -> list:
    with open("persos.pims", "rb") as flux:
        return pickle.load(flux)
    # flux.close()


def lireObjetsDepuisUnFichierObjet() -> list:
    with open("persos-bis.pims", "rb") as flux:
        persos = []
        while(True):
            try:
                persos.append(pickle.load(flux))
            except EOFError as err:
                break
        return persos
    # flux.close()


disney = Personnage.genererPersonnages()
print("Liste des personnages de travail")
afficherTousLesPersonnages(disney)

print("\nEcriture de la liste dans un fichier texte")
ecrireDansUnFichierTexte(disney)

print("\nLire la liste depuis un fichier texte")
[print(p) for p in lireDepuisUnFichierTexte()]

print("\nEcriture de la liste dans un fichier CSV")
ecrireDansUnFichierCSV(disney)

print("\nLire la liste depuis un fichier CSV")
[print("Je m'appelle", p.prenom, p.nom, "je suis un(e)", p.animal)
 for p in lireDepuisUnFichierCSV()]

print("\nLire la liste depuis un fichier CSV (bis)")
[print("Je m'appelle", p.prenom, p.nom, "je suis un(e)", p.animal)
 for p in lireDepuisUnFichierCSVBis()]

print("\nEcriture de la liste dans un fichier objet")
ecrireListeDansUnFichierObjet(disney)

print("\nEcriture des objets de la liste dans un fichier objet")
ecrireObjetsDansUnFichierObjet(disney)

print("\nLire la liste depuis un fichier objet")
[print("Je m'appelle", p.prenom, p.nom, "je suis un(e)", p.animal)
 for p in lireListeDepuisUnFichierObjet()]

print("\nLire les objets de la liste depuis un fichier objet")
[print("Je m'appelle", p.prenom, p.nom, "je suis un(e)", p.animal)
 for p in lireObjetsDepuisUnFichierObjet()]
