userName = "adminou"
userName1 = input("Lütfen kullanıcı adını giriniz:")\
    .lower()\
    .replace("ı", "i").replace("ü", "u").replace("ö", "o")\
    .replace("ş", "s").replace("ç", "c").replace("ğ", "g")

if userName == userName1:
    print("Giriş Yapıldı")
else:
    print("Kullanıcı adı hatalı")

