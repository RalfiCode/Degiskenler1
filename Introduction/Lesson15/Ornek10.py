from enum import Enum,unique,auto,Flag

class Renkler(Flag):
    Kırmızı  = auto()
    Sarı     = auto()
    Mavi     = auto()
    Yeşil    = auto()
    Pembe    = auto()
    Turunucu = auto()
    Beyaz    = Kırmızı | Mavi | Sarı

print(Renkler.Mavi and Renkler.Turunucu)
print(Renkler.Beyaz)