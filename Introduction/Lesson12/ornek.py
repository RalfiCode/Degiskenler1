girmail = input("mail veriniz:") 
girtel = input("telefon giriniz")
isim = girmail[0:girmail.index('.')]
soyad = girmail[girmail.index('.') + 1 : girmail.index('@')]
if girtel.startswith("0"):
    girtel[0] = " "
else: 
    pass
print("Isım: {}\nSoyisim: {}\nTelefon: +90{}\nMail: {}".format(isim,soyad,girtel,girmail))