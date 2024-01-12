
# program 1
def add(x,y):
    return x + y
q1 = add(12,4)
print(q1)

# program 2
add =  lambda x,y:x+y
q2 = add(13,4)
print(q2)

#program 3
sqr  = lambda x:x*x
e = sqr(2)
print(e)

#program 4
def additionAll(*args):
    print(args)
    total = 0
    for i in args:
        total = total  + i
    return total

f = additionAll(12,33,44,55,66,77,88,99,100,101)
print(f)

# program 5
def updateCity(**kwargs):
    print(kwargs)
    kwargs['city'] = "nagpur"
    return kwargs
f2 = updateCity(fullName = "chinmay",city = "pune", age= 34)
print(f2)

# program 6
def addition(x = 4,y= 6):
    print(x+y)
addition()
addition(1,2)

# program 7

def addition(x3,x2,x1):
    print(x3+x2+x1)
    print(x3)
addition(x1 = 3,x2 = 4,x3 = 10)





























