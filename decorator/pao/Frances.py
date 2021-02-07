from decorator.pao.Pao import Pao


class Frances(Pao):
    def __init__(self):
        pass


    @property
    def value(self):
        return 2

    @property
    def name(self):
        return "Francês"
