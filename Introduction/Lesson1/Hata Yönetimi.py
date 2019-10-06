try:
    sayi = int(input("Lütfen sadece sayısal veri giriniz: "))
    print("Gelen Sayı: ", sayi)
    print("Işlem sonu")
except ValueError as joni:
    print("Beklenmedik bir hata ile karşılaşıldı \nLütfen tekrar deneytiniz!")
    print("Sistem hatası: ",joni)
except ZeroDivisionError as lolo:
    print("Sistem hatası:", lolo)
finally:
    print("Her durumda çalışırım")