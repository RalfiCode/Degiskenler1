snvnotu = int(input("Sınav notunu giriniz: "))
if 0 <= snvnotu <= 30:
    print("FF aldınız!")
elif 30 < snvnotu <= 50:
    print("DD aldınız!")
elif 50 < snvnotu <= 70:
    print("CC aldınız!")
elif 70 < snvnotu <= 85:
    print("BB aldınız!")
elif 85 < snvnotu < 100:
    print("AA aldınız!")
else:
    print("Hatalı giriş yaptınız!")
