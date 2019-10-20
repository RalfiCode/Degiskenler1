def Hesapla(*sayilar) -> float:
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

result = Hesapla(1,2,3,4,5,6,7,8,9)
print(result)