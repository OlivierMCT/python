
class Personnage:
    @property
    def prenom(self) -> str: return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str) -> None: self.__prenom = prenom

    @property
    def nom(self) -> str: return self.__nom
    @nom.setter
    def nom(self, nom: str) -> None: self.__nom = nom

    @property
    def animal(self) -> str: return self.__animal
    @animal.setter
    def animal(self, animal: str) -> None: self.__animal = animal

    def __init__(self, prenom: str, nom: str, animal: str) -> None:
        self.prenom = prenom
        self.nom = nom
        self.animal = animal

    def __str__(self) -> str:
        return "{} {} ({})".format(self.prenom, self.nom, self.animal)

    @staticmethod
    def genererPersonnages() -> list:
        return [
            Personnage("Mickey", "Mouse", "souris"),
            Personnage("Donald", "Duck", "canard"),
            Personnage("Daisy", "Duck", "canard"),
            Personnage("Minnie", "Mouse", "souris"),
            Personnage("Balthazar", "Picsou", "canard"),
            Personnage("Clarabelle", "Cow", "vache")
        ]
