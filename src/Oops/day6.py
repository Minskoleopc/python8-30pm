

# Duck typing

class Human:
    def talk(self):
        print('Hello hi')
class Dog:
    def talk(self):
        print("Bow Bow")

def obj_talk(obj):
    obj.talk()

c = Human()
d = Dog()

obj_talk(c)
obj_talk(d)


# Operator overloading +
class BookY:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages

class BookZ:
    def __init__(self, pages):
        self.pages = pages

ramayan = BookY(200)
mahabharat = BookZ(150)
print(ramayan.pages+mahabharat.pages)
print(ramayan+mahabharat)

# Method overloading

class Calculator:
    # def addition(self,x,y):
    #     print(x+y)
    # def addition(self,x,y,z):
    #     print(x+y+y)
    # def addition(self ,x, y , z , a):
    #     print(x + y + z + a)


    def addition(self,x=None,y=None,z=None,b=None):
        if x != None and y != None and z != None and b != None:
            print(x+y+z+b)
        if x != None and y != None and z != None:
            print(x+y+z)
        if x != None and y != None:
            print(x+y)

a = Calculator()
a.addition(13,4)
a.addition(13,4,4)
a.addition(13,4,4,4)

# Method overriding




class WorldBank:
    def loan(self):
        print("I am  loan from WB")
    def save(self):
        print("I am save from WB")

class SBI(WorldBank):
    def loan(self):
        print("I am  loan from SBI")
    def save(self):
        print("I am save from SBI")


nagpur = SBI()
nagpur.save()
nagpur.loan()
