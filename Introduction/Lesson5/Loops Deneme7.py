from random import randint
i = 0
sayilar = []
while i <= 6:
    sayi = randint(1, 49)
    if sayilar.count(sayi):
       i -= 1
    else:
        sayilar.append(sayi)
    i += 1
print(sayilar[:])



