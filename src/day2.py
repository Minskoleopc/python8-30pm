
# program 1
x = 10
print(x)
print(type(x))
# 10, -90,0

# program 2

x1 = 10.9
print(x1)
print(type(x1))
#12.4 , 55.6 , 0.56

# program 3
z = True
print(z)
print(type(z))
# True or False

# program 4
d = "chinmay"
print(d)
print(type(d))
# "A","a","123@sda"," "

# collections

# string
e = "pune"
print(e)
print(type(e))

# list (multiple elements at one memory)
#listName = [ele,ele2,ele3]
cities = ["pune","mumbai","banglore","kolkata"]
marks = [11,22,33,44]
info = ["chinmay","deshpande",7709192441,True]
print(cities)
print(marks)
print(info)
print(type(cities))
cities.append("hindi")

# tuple (fixed length)
students = ("ram","sham","satish","sachin")
print(students)
print(type(students))
#students[4] = "chinmay"

marks = 8,10
print(type(marks))

# set (does not allow duplicate values)
names = {"chinmay","sarika","poorva","ram","chinmay"}
print(names)
print(type(names))

# dictionary
info2 = ["poorva","vyas",29,88]
info3 = {
    # property ---> value
    "firstName":"poorva",
    "lastName":"vyas",
    "age":29,
    "rollNo":88
}
print(type(info3))


