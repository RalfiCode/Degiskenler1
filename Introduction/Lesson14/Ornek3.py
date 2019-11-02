class BaseClass():
    def __init__(self, isim = "",soyisim = "",TCKN = "",telefon= ""):
        self.isim = isim
        self.soyisim = soyisim
        self.TCKN = TCKN 
        self.telefon = telefon
    def __str__(self):
        return "{} {} {} {}".format(self.isim,self.soyisim,self.TCKN,self.telefon)


class Personel(BaseClass):
    def __init__(self,maas, gorev ,isim = "",soyisim = "",TCKN = "",telefon= "" ):
         self.maas = maas
         self.gorev= gorev
         super().__init__(isim,soyisim,TCKN,telefon)
    def __str__(self):
        return super().__str__() + "{} {}".format(self.maas,self.gorev)

class Ogrenci(BaseClass):
    okul_no = ""
    sinif = ""
    mail = ""

class Ogretmen(Personel):
    brans = ""
    sinif = ""
    mail = ""

class MudurYardimcisi(Personel):
    mail = ""

class Mudur(Personel):
    mail = ""

class Memur(Personel):
    mail = ""

class Hizmetli(Personel):
    pass


personel = Personel("a1","a2","a3","a4")
print(personel)