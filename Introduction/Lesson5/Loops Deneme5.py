dizi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tekdizi = []
çiftdizi = []
i = 0
while i < len(dizi):
    i += 1
    if i % 2 == 0:
        çiftdizi.append(i)
    else:
        tekdizi.append(i)
print("Tek sayıların adedi: {}, Çift sayıların adedi: {}".format(len(tekdizi), len(çiftdizi)))
