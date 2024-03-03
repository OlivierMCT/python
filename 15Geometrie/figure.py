class Coordonnee:
    @property
    def x(self) -> int: return self.__x
    @x.setter
    def x(self, x: int) -> None: self.__x = x

    @property
    def y(self) -> int: return self.__y
    @y.setter
    def y(self, y: int) -> None: self.__y = y

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Figure:
    @property
    def couleur(self) -> str: return self.__couleur
    @couleur.setter
    def couleur(self, couleur: str) -> None: self.__couleur = couleur

    @property
    def centre(self) -> Coordonnee: return self.__centre
    @centre.setter
    def centre(self, centre: Coordonnee) -> None: self.__centre = centre

    def __str__(self) -> str:
        return "Centre ({},{}), Couleur: {}".format(self.centre.x, self.centre.y, self.couleur)

    def __init__(self, x: int, y: int, couleur: str) -> None:
        self.centre = Coordonnee(x, y)
        self.couleur = couleur


class Carre(Figure):
    @property
    def cote(self) -> int: return self.__cote
    @cote.setter
    def cote(self, cote: int) -> None: self.__cote = cote

    def __str__(self) -> str:
        return "Carre {}, Cote= {}".format(super().__str__(), self.cote)

    def __init__(self, x: int, y: int, cote: int, couleur: str) -> None:
        super().__init__(x, y, couleur)
        self.cote = cote


class Cercle(Figure):
    @property
    def rayon(self) -> int: return self.__rayon
    @rayon.setter
    def rayon(self, rayon: int) -> None: self.__rayon = rayon

    def __init__(self, x: int, y: int, rayon: int, couleur: str) -> None:
        super().__init__(x, y, couleur)
        self.rayon = rayon

    def __str__(self) -> str:
        return "Cercle {}, Rayon= {}".format(super().__str__(), self.rayon)

    @property
    def __dict__(self):
        return {
            "x": self.centre.x,
            "y": self.centre.y,
            "rayon": self.rayon,
            "couleur": self.couleur
        }
