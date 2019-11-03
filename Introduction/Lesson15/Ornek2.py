class Personel:
    def __init__(self,isim = "",soyisim= ""):
        self.Firstname = isim
        self.Lastname = soyisim
    
    @property
    def Email(self):
        return "{}.{}.gmail.com".format(self.Firstname.lower(),self.Lastname.lower())

    @property
    def isim_soyisim(self):
        return "{}-{}".format(self.Firstname,self.Lastname)
    
    
    @isim_soyisim.setter
    def isim_soyisim(self, parameters):
        ad,soyad = parameters.split(" ")
        self.Firstname = ad
        self.Lastname =  soyad

    @isim_soyisim.deleter
    def isim_soyisim(self):
        print("Kişi silindi")
        self.Firstname = None
        self.Lastname = None

personel = Personel("Ralfi","Bahar")
print(personel.Firstname)
print(personel.Lastname)
print(personel.Email)

personel.isim_soyisim = "moni koni"
print(personel.Firstname)
print(personel.Lastname)
print(personel.Email)

del personel.isim_soyisim
print(personel.Firstname)
print(personel.Lastname)
