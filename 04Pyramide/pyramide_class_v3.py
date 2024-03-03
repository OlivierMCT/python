class pyramide:
    @property
    def hauteur(self) -> int: return self.__hauteur
    @hauteur.setter
    def hauteur(self, hauteur: int) -> None:
        if(type(hauteur) is not int): 
            raise ValueError("hauteur non numérique")
        if(hauteur < 1): 
            raise ValueError("hauteur invalide")
        self.__hauteur = hauteur

    @property
    def symbole(self) -> str: return self.__symbole
    @symbole.setter
    def symbole(self, symbole: str) -> None:
        if(len(symbole) != 1): raise ValueError("symbole invalide")
        self.__symbole = symbole

    def __init__(self, hauteur: int, symbole: str = "*") -> None:
        self.hauteur = hauteur
        self.symbole = symbole

    def __genererLigne(self, etage): return " " * (self.hauteur - etage) + self.symbole * (etage * 2 - 1)

    def genererEtages(self) -> list: return [self.__genererLigne(i) for i in range(1, self.hauteur + 1)]

    def __str__(self) -> str: return "\n".join(self.genererEtages())
