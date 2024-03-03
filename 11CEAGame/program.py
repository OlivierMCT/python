
from random import randint
import sys
from game import Game

# python program.py -niveau 1000

arguments = sys.argv[1:]
try:
    niveau = int(arguments[arguments.index("-niveau") + 1])
except:
    print("l'option -niveau est obligatoire")
    exit(-1)

print("📢 Bienvenue dans le CEA Game !")
print()
jeu = Game()

try:
    while True:
        jeu.start(niveau)
        while True:
            tentative = int(input("[tentative]> "))
            if(tentative == -1):
                magic = jeu.cancel()
                raise Exception()

            res = jeu.play(tentative)
            if(res == 0):
                break
            elif(res < 0):
                print("trop petit")
            else:
                print("trop grand")
            print()
        print("👏 Bravo | ✨ Score =", jeu.score)

        if(input("[Encore (O/N)]> ") != "O"):
            break
except Exception as ex:
    print("Il fallait trouver:", magic)
                
print("Bye bye")