import math
def karekokhesapla(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return math.sqrt(toplam)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 88, 99]

result = karekokhesapla(numbers)
print("İşlem sonucu: ", result)