
# Abstrat class

# class Myclass:
#     def calculate(self,x):
#         print(x)
#
# obj = Myclass()
# obj.calculate(1)
# obj1 = Myclass()
# obj.calculate(2)
# obj2 = Myclass()
# obj2.calculate(3)


#cube

#squareroot

#square


from abc import  ABC,abstractmethod

class myClass(ABC):
    @abstractmethod
    def Calculate(self,x):
        pass

class Square(myClass):
    def Calculate(self, x):
        print('Square')
class Cube(myClass):
    def Calculate(self, x):
        print("Cube")

class SquareRoot(myClass):
    def Calculate(self, x):
        print("SquareRoot")

# we cannot create object of abstract class
# abstract class can have - abstract method and non - abstract method
# it mandatory for class to implement abstract method if inherited

class Vehicle(ABC):
    @abstractmethod
    def wheel(self, x):
        pass
    def Country(self):
        print("India")

class Maruti(Vehicle):
    def wheel(self, x):
        print("4 wheels")


class Audi(Vehicle):
    def wheel(self, x):
        print("5 wheels")

a = Audi()
a.wheel(5)
a.Country()

b = Maruti()
b.wheel(4)
b.Country()















a = Cube()
b = Square()
c = SquareRoot()

a.Calculate(12)
b.Calculate(34)
c.Calculate(56)
