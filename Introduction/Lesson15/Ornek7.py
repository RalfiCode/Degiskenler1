from enum import Enum,unique

@unique
class Icecek(Enum):
    Vanilya  = 7
    Cikolata = 4
    Visne    = 3
    Muz      = 1
    Kiraz    = 7

for x in Icecek:
    print(x)
    print("-" * 30)

for x,y in Icecek.__members__.items():
    print(x,y,y.value)
    print("-" * 30)
