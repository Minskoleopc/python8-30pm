

# inheritance
#
# class Mother:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#     def displayM(self):
#         print(self.firstName + self.lastName)
# class Father:
#     def __init__(self, fn, ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayF(self):
#         print(self.firstName + self.lastName)
#
# class Son(Mother,Father):
#     def __init__(self,fn, ln,sn):
#         super().__init__(fn, ln)
#         self.sname = sn
#
#     def displayS(self):
#         print(self.sname + self.lastName)
#
# chinmay = Son("shrish","deshpande","chinmay")

# Method resolution order

class A(object):
    def method(self):
        print('A class is called') # 3
        super().method()

class B(object):
    def method(self):
        print('B class is called') #5
        super().method()

class C(object):
    def method(self):
        print('C class is called') # C

class X(A,B):
    def method(self):
        print("X is called") # 2
        super().method()

class Y(B,C):
    def method(self):
        print("Y is called") #4
        super().method()
class P(X,Y,C):
    def method(self):
        print("P is called") # 1
        super().method()

p = P()
p.method()







    









