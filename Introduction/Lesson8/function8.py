def mail() -> str:
    isim = input("Isim igiriniz: ")
    soyad = input("Soyad giriniz: ")
    domain = input("Domain giriniz: ")
    if not domain:
        return "{}.{}@bilgeadam.com".format(isim,soyad)
    else:
        return "{}.{}@{}".format(isim,soyad,domain)

a = mail()
print(a)
print(type(a))
print("Mail metodunun geriye dönüş tipi", mail.__annotations__)