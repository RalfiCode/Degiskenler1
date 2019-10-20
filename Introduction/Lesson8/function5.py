# Kullanıcı dışarıdan dilediği kadar sayı girecek, her sayı girdikten sonra, sayı girmeye devam edip etmeyeceği sorulacak. :)

# kullanıcı y Y tuşuna basarsa, yeni bir sayı girmesi istenilecek
# kullanıcı harici bir tuşa basar ise, içeriye aldığı sayılar içerindeki tek sayılar içerisinde yer alan en büyü ve en küçün sayının biribirine olan farkını geriye dönecek :)


# https://www.packtpub.com/free-learning

liste = []
def gir():
    i =input("Sayı girmek ister misiniz y/n: ")
    while i == "y" or i == "Y":
        a = int(input("sayı giriniz:"))
        i = input("Sayı girmek ister misiniz y/n: ")
        liste.append(a)


gir()
sadecetek = [sayi for sayi in liste if sayi % 2 == 1]
print(max(sadecetek) - min(sadecetek))
