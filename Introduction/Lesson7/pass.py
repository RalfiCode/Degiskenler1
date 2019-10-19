while True:
    sifre = input("Lütfen parola belirleyiniz: ")
    if not sifre:
        continue
        #pass
    elif len(sifre) in range(3, 8):
        print("Şifreniz: ", sifre)
    else:
        print("parola 8 karekterden uzun veya 3 karekterden kısa olmamalıdır")
