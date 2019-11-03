from enum import Enum

class Color(Enum):
    Red   = 1
    Green = 2
    Blue  = 3


print(Color.Blue)
print(repr(Color.Green))
print(type(Color.Red))

print(isinstance(Color.Red, Color))
print(Color.Red.name)