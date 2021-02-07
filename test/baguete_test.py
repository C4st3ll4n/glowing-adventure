import unittest

from decorator.pao.Baguete import Baguete
from decorator.pao.Baguete import Baguete
from decorator.recheio.Calabresa import Calabresa
from decorator.recheio.Salame import Salame


class BagueteTestCase(unittest.TestCase):
    def test_baguete_price(self):
        baguete = Baguete()
        self.assertEqual(baguete.value, 5)

    def test_baguete_with_salame_price(self):
        baguete = Salame(Baguete())
        self.assertEqual(baguete.value, 7)

    def test_baguete_with_calabresa_price(self):
        baguete = Calabresa(Baguete())
        self.assertEqual(baguete.value, 9)

    def test_baguete_with_calabresa_and_salame_price(self):
        baguete = Salame(Calabresa(Baguete()))
        self.assertEqual(baguete.value, 11)

    def test_baguete_with_salame_and_calabresa_price(self):
        baguete = Calabresa(Salame(Baguete()))
        self.assertEqual(baguete.value, 11)


if __name__ == '__main__':
    unittest.main()
