class Employee:
    '''
    Açıklama alanı ekleyebilirsiniz
    bu satırları görüntülemek için, .__doc__ nesnesini kullanabilirsinz
    
    FirstName : Kişinin Adı
    LastName  : Kişinin Soyadı
    Phone     : Kişinşn Telefonu
    Mail      : Kişinin Maili
    
    '''

personel = Employee()
print(personel.__doc__)

personel.FirstName = "Ralfi"
personel.LastName  = "Bahar"
personel.Mail      = "ralfibahar2005@hotmail.com"
personel.Phone     = "+905399125147"

print(personel)
print(personel.FirstName)