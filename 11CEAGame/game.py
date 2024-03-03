from random import randint


class Game:
    @property
    def score(self) -> int: return self.__score

    def __init__(self) -> None:
        self.__score = 0
        self.__isPlaying = False

    def start(self, max: int) -> None:
        self.__isPlaying = True
        self.__score = 0
        # genération d'un nombre aléatoire entre 0 et 100
        self.__magic = randint(0, max if max > 0 else max * -1)

    def play(self, number: int) -> int:
        if(self.__isPlaying == False):
            raise RuntimeError("no party :/")
        self.__score += 1
        resultat = number - self.__magic
        if(resultat == 0):
            self.__isPlaying = False
        return resultat

    def cancel(self) -> int:
        if(self.__isPlaying == False):
            raise RuntimeError("no party :/")
        self.__isPlaying = False
        return self.__magic
