from datetime import datetime
from datetime import timedelta

class Personel:
    FirstName = ""
    LastName  = ""
    Mail      = ""
    Phone     = ""
    Adress    = ""
    FireDays  = ""
    HireDate  = "{}/{}/{} {}:{}".format(
        datetime.now().day,
        datetime.now().month,
        datetime.now().year, 
        datetime.now().hour,
        datetime.now().minute
    )

    def IseAl(self):
        print("""
        Personel Adı :                  {}
        Personel Soyadı :               {}
        Personel Mail :                 {}
        Personel Telefon :              {}
        Personel Adres :                {}   
        Personel Işe Giriş Tarihi :     {}
        Peronel Sözleşme Bitiş Tarihi : {}

        Personelin Işe Girişi Tamamlandı!
        """.format( self.FirstName,
         self.LastName,
          self.Mail,
           self.Phone,
            self.Adress,
             self.HireDate,
              "{}/{}/{} {}:{}".format(
              (datetime.now() + timedelta(days = self.FireDays)).day,
              (datetime.now() + timedelta(days = self.FireDays)).month,
              (datetime.now() + timedelta(days = self.FireDays)).year,
              (datetime.now() + timedelta(days = self.FireDays)).hour,
              (datetime.now() + timedelta(days = self.FireDays)).minute
              )))




calisan = Personel()
calisan.FirstName = "Ralfi"
calisan.LastName  = "Bahar"
calisan.Mail      = "ralfibahar2005@hotmail.com"
calisan.Phone     = "05399125147"
calisan.Adress    = "Beşiktaş"
calisan.FireDays  = 150
print(calisan.IseAl())