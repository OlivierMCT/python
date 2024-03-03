class fractionError(BaseException):
  @property
  def numero(self) -> int: return self.__numero
  
  @numero.setter
  def numero(self, numero: int) -> None: self.__numero = numero

  def __init__(self, numero: int, message: str) -> None:
      super().__init__(message)
      self.numero = numero



