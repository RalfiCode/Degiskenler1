deger = sorted("çöğüşlbilge adam")
print(deger)

import locale
locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")

deger2 = sorted("çgöhjğübilge adam", key=locale.strxfrm)
print(deger2)