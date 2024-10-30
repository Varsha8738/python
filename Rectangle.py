class Rectangle:
    def __init__(self,l,w):
        self.__l = l
        self.__w = w
    def area(self):
        return self.__l * self.__w
    def perimeter(self):
        return 2 *(self.__l + self.__w)
rect = Rectangle(5,3)
print(f"Area: {rect.area()}")
print(f"Perimeter:{rect.perimeter()}")
Output :
Area: 15
Perimet
