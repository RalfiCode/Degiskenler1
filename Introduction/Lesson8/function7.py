def turozel():
    listetr = ["ı", "ş","ğ","ü","ç","ö"]
    listetr1 = ["i", "s","g","u","c","o"]
    a = input("Mailinizi giriniz: ")
    i = 0
    while i < len(a):
        if a[i] == listetr[i]:
            a[i] = listetr1[i]
        else:
            pass
    print(a)
    i += 1
    return a



b = turozel()
print(b)
