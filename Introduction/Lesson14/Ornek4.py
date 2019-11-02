class Cup1():
    def __init__(self):
        self.color = None
        self.content = None
    
    def fill(self, beverage):
        self.content = beverage
    
    def empty(self):
        self.content = None
    
    def __str__(self):
        return self.color + " " + self.content

cup1 = Cup1()
cup1.color = "Red"
cup1.content = "Water"
print(cup1)

cup1.empty()
cup1.color  = "Black"
cup1.content = "Coffee"
print(cup1)

class Cup2():
    def __init__(self):
        self.color = None
        self._content = None
    
    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None

    def __str__(self):
        return self.color + " " + self._content

cup2 = Cup2()
cup2.color = "Green"
cup2._content = "Cola"
print(cup2)

class Cup3():
    def __init__(self,color):
        self.color = color
        self.__content = None
    
    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def __str__(self):
        return self.color + " " + self.__content

#cup3.color = "Blue"
#cup3.__content = "Fanta"
cup3 = Cup3("Bluee")
cup3._Cup3__content = "Fanta"
print(cup3)