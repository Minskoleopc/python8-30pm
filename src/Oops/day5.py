
# polymorphhism
#Duck typing
# class Duck:
#     def talk(self):
#         print("Quack Quack")
# class Human:
#     def talk(self):
#         print("Hello hi ")
#
# class Dog:
#     def talk(self):
#         print("Bow Bow")
#
# def call_talk(obj):
#     obj.talk()
#
# a = Dog()
# b = Human()
# c = Duck()
#
# call_talk(a)
# call_talk(b)
# call_talk(c)

# program 2

class Duck:
    def talk(self):
        print("Quack Quack")
class Human:
    def talk(self):
        print("Hello hi ")

class Dog:
    def talk(self):
        print("Bow Bow")

class Cat:
    def sound(self):
        print("Meow Meow")

def call_talk_sound(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'sound'):
        obj.sound()

a = Dog()
b = Human()
c = Duck()
d = Cat()
call_talk_sound(a)
call_talk_sound(b)
call_talk_sound(c)
call_talk_sound(d)

#Operator overloading

print(1 + 1)
print("1"+ "1")

class BookX:
    def __init__(self,x):
        self.pages = x
    def __add__(self, other):
        return self.pages + other.pages

class BookY:
    def __init__(self,y):
        self.pages = y

ramayan = BookX(1000)
mahabharat = BookY(450)
print(ramayan + mahabharat)
#print(ramayan.pages + mahabharat.pages)

# program 4


class BookA:
    def __init__(self,x):
        self.pages = x


class BookB:
    def __init__(self,y):
        self.pages = y
    def __gt__(self, other):
        return self.pages > other.pages

atomicHabits = BookA(24)
geeta = BookB(2344)
#print(atomicHabits.pages > geeta.pages)
print(geeta > atomicHabits)








# overlaoding



# overriding