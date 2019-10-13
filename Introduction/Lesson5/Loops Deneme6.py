sesli_harfler = ["a", "e", "o", "ö", "ü", "u", "ı", "i"]
sesli = []
sessiz = []
i = 0
girilen = input("Metin Giriniz: ").lower()
while i < len(girilen):
    adet = sesli_harfler.count(girilen[i])
    if sesli_harfler.count(girilen[i]):
        sesli.append(girilen[i])
    else:
        sessiz.append(girilen[i])
    i += 1
print("Metinde sesli harf sayısı: {}, sessiz harf sayısı: {}".format(len(sesli), len(sessiz)))




