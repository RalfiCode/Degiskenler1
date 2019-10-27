class Ogrenci:
    Adı = ""
    def Kaydet(self,):
        print(self.Adı,"Adlı öğrencinin giriş işlemleri yapıldı")
    
    def NotVer(self,Ogrenci_not):
        print(Ogrenci_not,"Adli öğrenciye not verildi")

    def CezaVer(self,Ogrenci_ceza_ver):
        print(Ogrenci_ceza_ver,"Adli öğrenciye ceza verildi")

    def YoklamaGir(self, Ogrenci_Yokla):
        print(Ogrenci_Yokla,"Adli öğrencinin yoklaması girildi")
    
ogr = Ogrenci()
ogr.Adı = "Ralfi Bahar"
ogr.Kaydet()

Ogrenci.CezaVer("","Ralfi Bahar")
Ogrenci.YoklamaGir("","Ralfi Bahar")

Ogrenci().CezaVer("ss")