try:
    snvnot = int(input("Sınav notu giriniz: "))
    if snvnot < 0:
        print("0'dan küçük not giremezsiniz")
    elif snvnot > 100:
        print("100'den büyük not giremezsiniz")
    else:
        print("Sınav notunuz:", snvnot)
except ValueError:
    print("Lütfen sayısal veri giriniz.")
finally:
    pass
