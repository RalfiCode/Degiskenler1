class Personel:
    FirstName = ""
    LastName = ""
    Mail = ""
    Phone = ""
    def __str__(self):
        return "{} {}".format(self.FirstName,self.LastName)

calisan1 = Personel()
calisan1.FirstName = "Ralfi"
calisan1.LastName = "Bahar"
calisan1.Mail = "ralfibahar2005@hotmail.com"
calisan1.Phone = "05399125147"

calisan2 = Personel()
calisan2.FirstName = "Meri"
calisan2.LastName = "Istiroti"
calisan2.Mail = "meri.istiroti@gmail.com"
calisan2.Phone = "05325487653"

print(calisan1) 
print(calisan2)