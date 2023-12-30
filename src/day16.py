

#tuple
listA = [11,22,33,44,55,66]
print(listA)
print(type(listA))

h = (2,3,4)
print(h)
print(type(h))

h1 = 1,3
print(h1)
print(type(h1))


# why tuple ???
names = ["chinmay","sarika","poorva","ashish","ram"]
names.append("sarika")
print(names)
names[0] = "tanmay"
print(names)

#           0       1          2        3
cities = ("pune","mumbai","banglore","kolkata")
# can we access tuple by index
print(cities[0])

# using range() function
for x in range(len(cities)):
    print(x)
    print(cities[x])

# without range()
fruits = "apple","mango","grapes"
for item in fruits:
    print(item)

#fruits[0] = "banana"
fruits = ("apple","mango","grapes","mango")
print(len(fruits))

# del fruits
# print(fruits)

animals = ('tiger',"lion","rabbit","tiger")
# x = animals[0]
# y = animals[1]
# z = animals[2]

x,y,z,e = animals
print(x)
print(y)
print(z)
print(e)

c1 = animals.count("tiger")
print(c1)

q1 = animals.index("tiger")
print(q1)


# various ways to import functions and methods in python

# what are modules
# what are packages , how to pacakages
# what are libraries and how to create libraries

# how to import module , packages and libraries