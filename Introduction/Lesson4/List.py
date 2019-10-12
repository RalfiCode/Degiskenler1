cities = ["Adana", "Ankara", "Istanbul", "Antalya", "Edirne", "Malatya"]
# print(cities[0], sep='\n')
print("\n".join(cities))


lastIndex = len(cities) - 1
print(cities[lastIndex])

print(cities[2:5])

print('B' in cities)

x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
a = list(zip(x, y, z))
print(a[0])
