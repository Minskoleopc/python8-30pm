# program
# class Calculator:
#     # class level variable
#     c = 10
#     def __init__(self,x,y,z):
#         # instance variable
#         self.x = x
#         self.y = y
#         self.z = z
#
# amol = Calculator(122,133,144)
# chinmay = Calculator(121,131,141)
# print(amol.x)
# print(amol.y)
# print(amol.z)
# print(amol.c)
#
# print(chinmay.x)
# print(chinmay.y)
# print(chinmay.z)
# print(chinmay.c)
# chinmay.c = 99
#
# print(amol.c)
# print(chinmay.c)

# program 2 changing value of instance level variable

class CalculatorB:
    a = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # instance level method
    def changeX(self,change):
        self.x = change

chinmayC = CalculatorB(12,3)
print(chinmayC.x)
print(chinmayC.y)
chinmayC.changeX(45)
print(chinmayC.x)


class CalculatorC:
    c = 10
    def __init__(self ,x,y):
        self.x = x
        self.y = y

    @classmethod
    def changeC(cls,ch):
        cls.c = ch
bimal = CalculatorC(3,4)
print(bimal.x)
print(bimal.y)
print(bimal.c)
tavish = CalculatorC(13,14)
print(tavish.x)
print(tavish.y)
print(tavish.c)
CalculatorC.changeC(45)
print(bimal.c)
print(tavish.c)

bimal.c = 99
print(tavish.c)
print(bimal.c)



