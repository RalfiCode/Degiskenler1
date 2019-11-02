class Calisan():
    
    def __init__(self,isim,soyisim,maas,departman,yas = 10):
        print("Çalışanın sınıfının yapıcı metodu çalıştı")
        self.Firstname = isim
        self.LastName = soyisim
        self.Salary = maas
        self.Department = departman
        self.Age = yas

    def __str__(self):
        return "Personel Adı: {}\nPersonel Soyadı: {}".format(self.Firstname, self.LastName)
    
    def Info(self):
        print("Personel Adı: {}\nPersonel Soyadı: {}\nPersonel Departmanı: {}\nPersonel Yaşı: {}\nPersonel Maaşı: {}"
        .format(self.Firstname, self.LastName, self.Department, self.Age, self.Salary))
    
    def Raise(self, raiseRate):
        print("Çalışanın maaş bilgisi güncellendi")
        _salary = self.Salary
        self.Salary += raiseRate
        print("{} adlı personelin maaşı {}'(dan-den) {}'(a-e) güncellenmiştir)".format((self.Firstname + " " + self.LastName), _salary, self.Salary))

    def Change(self, changeDepartment):
        print("personelin departmanı değiştirlidi")
        _department = self.Department
        self.Department = changeDepartment
        print("{} adlı personelin departmanı {}'(dan-den) {}'(a-e) güncellenmiştir)".format((self.Firstname + " " + self.LastName), _department, self.Department))

personel = Calisan("Ralfi", "Vuranok", 999.999, "öğrenci", 14)
print(personel)
personel.Info()
personel.Raise(999.999)
personel.Change("Yazılım")

class Yonetici(Calisan):
    def __init__(self,isim,soyisim,maas,departman,calisansayisi,yas = 10):
        print("Yöneticinin sınıfının yapıcı metodu çalıştı")
        self.Firstname = isim
        self.LastName = soyisim
        self.Salary = maas
        self.Department = departman
        self.Age = yas
        self.Numberofemployee = int(calisansayisi)

    def print_base(self):
        for base in self.__class__.__bases__:
            print("Miras aldığı sınıflar : "+ base.__name__)

    def __str__(self):
        return "{} {} {}".format(self.Firstname, self.LastName, self.Department)

yonetici = Yonetici("Ralfi", "Bahar", 999999999, "yazılım", 1, 14)
yonetici.Info()
yonetici.print_base()