def mailadresicreate(isim, soyisim):
    _isim = "{}{}".format(isim[0:2].upper(), isim[2:].lower())
    _soyisim = soyisim.replace("a","e").lower()
    return "{}.{}@hotmail.com".format(_isim, _soyisim)




mail = mailadresicreate(input("Lütfen adınızı giriniz: "), input("Lütfen soyadınızı giriniz: "))
print(mail)