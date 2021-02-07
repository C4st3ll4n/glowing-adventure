from decorator.pao.Pao import Pao
from decorator.recheio.RecheioDecorator import RecheioDecorator


class Calabresa(RecheioDecorator):

    def __init__(self, pao: Pao):
        self.pao = pao

    @property
    def value(self) -> int:
        return 4 + self.pao.value

    @property
    def name(self) -> str:
        return f"{self.pao.name}, Calabresa"
