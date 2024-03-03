from fractions import Fraction
from fractionerror_class import fractionError
class fraction: #(object):
    @property
    def numerateur(self) -> int: return self.__numerateur
    
    @numerateur.setter
    def numerateur(self, num) -> None: self.__numerateur = num

    def __getDenominateur(self) -> int: # Obtenir Denominateur
        return self.__denominateur
    
    def __setDenominateur(self, den) -> None: # Modifier Denominateur
        if(den == 0):
            raise fractionError(101, "dénominateur invalide")
        self.__denominateur = den
    # Propriété
    denominateur = property(__getDenominateur, __setDenominateur)

    # constructeur
    def __init__(self, num: int, den: int = 1):
        # Attributs
        self.numerateur = num
        self.denominateur = den

    def afficher(self):
        # self: instance courante
        print(self.numerateur, "/", self.denominateur, sep="")

    def transformerEnChaine(self) -> str:
        return "{0:>2}/{1:<2}".format(self.numerateur, self.denominateur)

    def calculerQuotient(self) -> float:
        return self.numerateur / self.denominateur

    def reduire(self) -> None:
        leMin = min(self.numerateur, self.denominateur)
        for i in range(leMin, 1, -1):
            if(self.numerateur % i == 0 and self.denominateur % i == 0):
                self.numerateur = self.numerateur // i
                self.denominateur //= i
                break

    def __str__(self) -> str:
        return self.transformerEnChaine()

    def __add__(self, other):
        return fraction(
            self.numerateur * other.denominateur + self.denominateur * other.numerateur,
            self.denominateur * other.denominateur    
        )

    def __sub__(self, autre): raise NotImplementedError()
    def __mul__(self, autre): raise NotImplementedError()
    def __truediv__(self, autre): raise NotImplementedError()
    def __floordiv__(self, autre): raise NotImplementedError()
    def __mod__(self, autre): raise NotImplementedError()

    def __eq__(self, autre) -> bool: raise NotImplementedError()
    def __ne__(self, autre) -> bool: return not (self == autre)
    def __gt__(self, autre) -> bool: raise NotImplementedError()
    def __ge__(self, autre) -> bool: return (self > autre) or (self == autre)
    def __lt__(self, autre) -> bool: raise NotImplementedError()
    def __le__(self, autre) -> bool: return (self < autre) or (self == autre)

