def tekcift(a):
    if a == 0:
        return 0
    elif a % 2 == 0:
        return 1
    else:
        return -1
result = tekcift(int(input("Lütfen bir sayı giriniz: ")))
print(result)
