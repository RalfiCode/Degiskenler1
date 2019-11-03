import datetime

now = datetime.datetime.now()

print(str(now))
print(repr(now))

class Personel():
    def __init__(self,firstname):
        self.Firstname = firstname

    def __repr__(self):
        return "Personel({} {})".format(self.Firstname, self.Firstname)

    def __str__(self):
        return "{}-{}".format(self.Firstname,self.Firstname)

per = Personel("Ralfi")
print(str(per))
print(per)
print(repr(per))

print(per.__repr__())
print(per.__str__())