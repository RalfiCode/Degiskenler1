a = 1
tek = 0
cift = 0
while a <= 1000:
    if a % 2 == 0:
        cift += 1
    else:
        tek += 1
    a += 1
print("Çift sayıların toplamı: {}\ntek sayıların toplamı: {}".format(cift, tek))
