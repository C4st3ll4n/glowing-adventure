from abc import ABC


class Pao(ABC):

    def __init__(self, nome, valor):
        self._nome = nome
        self._valor = valor

    def value(self) -> int:
        return self._valor

    def name(self) -> str:
        return self._nome
