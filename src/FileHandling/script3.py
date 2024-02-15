# program 1
f1 = open('virat-kohli.png','rb')
f2 = open('virat2.png','wb')
bytes = f1.read()
f2.write(bytes)
f1.close()
f2.close()

# program 2

# with open('sample.txt','w') as f:
#     f.write("I am learning js \n")
#     f.write("I am learning python \n")
#
# with open('sample.txt','r') as f:
#     for line in f:
#         print(line)


# program 3

#python object  -----> binary file -----> serialization
#binary object  ------> python object  - deserialization

class Employee:
    def __init__(self,fn,ln,age,rollNo):
        self.firstName = fn
        self.lastName = ln
        self.age  = age
        self.rollNo = rollNo

#amol = Employee("amol","rao","23",45)
#
# import pickle
#
# f = open('emp.dat','wb')
# n = int(input('How many employee?')) # 2
#
# for i in range(n):
#     fn = input("Enter firstName")
#     ln = input("Enter lastName")
#     ag = input("Enter age")
#     rn = input("Enter rollNo")
#     e = Employee(fn,ln,ag,rn)
#     pickle.dump(e,f)
# f.close()
#
#


import pickle

f = open('emp.dat','rb')
while True:
    try:
        e =  pickle.load(f)
        print(e.firstName)
        print(e.lastName)
        print(e.lastName)
        print(e.lastName)
    except EOFError:
        print("End of file reached")
        break





