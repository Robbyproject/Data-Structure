class Circle:
    def __init__(self,radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius


    @radius.setter
    def radius(self,value):
        if value >= 0:
            self.__radius = value
        else:
            raise ValueError("Radius Can")

Cir = Circle(10)
print(Cir.radius)

Cir.radius = 20
print(Cir.radius)