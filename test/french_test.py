import unittest

from decorator.pao.Baguete import Baguete
from decorator.pao.Frances import Frances
from decorator.recheio.Calabresa import Calabresa
from decorator.recheio.Salame import Salame


class FrenchTestCase(unittest.TestCase):
    def test_french_price(self):
        french = Frances()
        self.assertEqual(french.value, 2)

    def test_french_with_salame_price(self):
        french = Salame(Frances())
        self.assertEqual(french.value, 4)

    def test_french_with_calabresa_price(self):
        french = Calabresa(Frances())
        self.assertEqual(french.value, 6)

    def test_french_with_calabresa_and_salame_price(self):
        french = Salame(Calabresa(Frances()))
        self.assertEqual(french.value, 8)

    def test_french_with_salame_and_calabresa_price(self):
        french = Calabresa(Salame(Frances()))
        self.assertEqual(french.value, 8)


if __name__ == '__main__':
    unittest.main()
