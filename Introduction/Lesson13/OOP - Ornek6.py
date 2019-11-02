class Employee:
    isim = ""
    soyisim = ""
    telefon = ""
    mail = ""

    def __str__(self):
        return "{} \n{} \n{} \n{}".format(self.isim,self.soyisim,self.telefon,self.mail)

emp = Employee()
emp.isim = "Ralfi"
emp.soyisim = "Bahar"
emp.telefon  = "05399125147"
emp.mail = "ralfi.bahar@gmail.com"

print  (emp)