sayi1 = int(input("Lütfen birinci sayiyi giriniz: "))
sayi2 = int(input("Lütfen ikinci sayiyi giriniz: "))
ne = input("Lütfen islemi belirtin: ")
if (ne == "topla"):
    print(sayi1 + sayi2)
elif (ne == "çikar"):
    print(sayi1 - sayi2)
elif (ne == "çarp"):
    print(sayi1 * sayi2)
elif (ne == "böl"):
    print(sayi1 + sayi2)
else:
    print(sayi1%sayi2)
