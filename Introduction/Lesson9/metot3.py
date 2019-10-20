def Metot(Ad, Soyad, Telefon, Gorev, *params):
    print(Ad, Soyad, Telefon, Gorev," ".join(params))

Metot("Ralfi", "Bahar", "05399125147", "ogrenci", "Hisar Lisesi")


def Metot2(*params):
    for p in params:
        print(p)
Metot2("a")

def Metot3(**params):
    for p in params:
        print("{0:<15}: {1}".format(p,params[p]))

Metot3(
    Firstname ="Ralfi",
    Lastaname ="Bahar",
    Phone = "05399125147",
    Mail = "ralficode@hotmail.com"
    )