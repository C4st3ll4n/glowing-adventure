from decorator.pao.Pao import Pao


class Baguete(Pao):
    def __init__(self,):
        pass

    @property
    def value(self):
        return 5

    @property
    def name(self):
        return "Baguete"
