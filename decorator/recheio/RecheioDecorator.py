from decorator.pao.Pao import Pao


class RecheioDecorator(Pao):
    def __init__(self):
        self._nome = None
        self._valor = None

    @property
    def value(self):
        return self._valor

    @property
    def name(self):
        return self._nome
