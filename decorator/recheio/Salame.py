from decorator.pao.Pao import Pao
from decorator.recheio.RecheioDecorator import RecheioDecorator


class Salame(RecheioDecorator):

    def __init__(self, pao: Pao):
        self.pao = pao

    @property
    def value(self):
        return 2 + self.pao.value

    @property
    def name(self):
        return f"{self.pao.name}, Salame"
