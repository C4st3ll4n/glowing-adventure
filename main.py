from decorator.pao.Baguete import Baguete
from decorator.pao.Frances import Frances
from decorator.recheio.Calabresa import Calabresa
from decorator.recheio.Salame import Salame

frances = Calabresa(Salame(Frances()))
print(f"{frances.name} -- R${frances.value}")


baguete = Salame(Calabresa(Baguete()))
print(f"{baguete.name} -- R${baguete.value}")
