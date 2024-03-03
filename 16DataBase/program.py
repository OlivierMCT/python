# Table
# - Colonne (nom, type, contrainte)
# - Cle Primaire (id numérique autoincrementer)
# - Cle etrangere (relation)

# SQL -> Action sur les données
# Creation Table
# Selection de données
# Mise à jour de données

import sqlite3
from personnage import *

def creerTable(cn: sqlite3.Connection):
  ordre = """
    Create Table If Not Exists Personnages (
      Id INTEGER PRIMARY KEY AUTOINCREMENT,
      Nom VARCHAR(100) NOT NULL,
      Prenom VARCHAR(100) NOT NULL,
      Animal VARCHAR(100) NULL
    )
  """
  cn.cursor().execute(ordre)
  cn.commit()
  print("Création de la table Personnages")

def insererDonnees(cn: sqlite3.Connection):
  ordre = """
    Insert into 
    Personnages (prenom, nom, animal) 
    Values ('Olivier', 'Astre', 'formateur')
  """
  cn.cursor().execute(ordre)
  cn.commit()

def insererDonneesVolume(cn: sqlite3.Connection):
  ordre = """
    Insert into 
    Personnages (prenom, nom, animal) 
    Values (?, ?, ?)
  """

  persos = Personnage.genererPersonnages()
  #cn.cursor().execute(ordre, (persos[0].prenom, persos[0].nom, persos[0].animal))
  cn.cursor().executemany(
    ordre, 
    [(p.prenom, p.nom, p.animal) for p in persos]
  )
  cn.commit()

def modifierDonnees(cn: sqlite3.Connection):
  ordre = """
    Update Personnages 
    Set animal = ?
    Where Id = 1 and nom = 'Astre'
  """
  
  cn.cursor().execute(ordre, ('lézard',))
  cn.commit()

def supprimerDonnees(cn: sqlite3.Connection):
  ordre = """
    Delete  From Personnages 
    Where Animal is NULL
  """
  
  cn.cursor().execute(ordre)
  cn.commit()

def selectionnerDonnees(cn: sqlite3.Connection):
  ordre = """
    Select distinct  Nom, Prenom, Animal
    From Personnages
    Where Nom like ?
    Order By Nom DESC, Prenom DESC
    Limit 2 offset 1
  """
  curseur = cn.cursor()
  curseur.execute(ordre, ('%e%',))
  for ligne in curseur.fetchall():
    print(ligne)

def selectionnerScalar(cn: sqlite3.Connection):
  ordre = """
    Select Count(*)
    From Personnages
    Where Animal = ?
  """
  curseur = cn.cursor()
  curseur.execute(ordre, ('canard',))
  print("Nombre de canards =", curseur.fetchone()[0])

try:
  with sqlite3.connect("maBase.db") as connexion:
    print("Ouverture de la connexion")

    #creerTable(connexion)
    #insererDonnees(connexion)
    #insererDonneesVolume(connexion)
    #modifierDonnees(connexion)
    #supprimerDonnees(connexion)

    selectionnerDonnees(connexion)
    selectionnerScalar(connexion)
    
    print("Fermeture de la connexion")
except sqlite3.Error as err:
  print("Oooops :/", err)
