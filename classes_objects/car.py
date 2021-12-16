class Car:
    wheels = 4 # class variable
    def __init__(self): #instance variables
        self.mil = 10 
        self.brand = "Audi"

c1 = Car()
c2 = Car()

c1.mil = 14
 
Car.wheels=6

print(c1.mil, c1.brand, c1.wheels)
print(c2.mil, c2.brand, c2.wheels)