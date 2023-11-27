
names = ["chinmay","sam","sarika"]

print(names)
names2 = names
print(names2)
print(names)
names2[1] = "sameer"

print(names)
print(names2)



# remove()
cities = ["mumbai","banglore","kolkata"]
cities.remove("mumbai")
print(cities)

# pop()
#           0           1          1
cities2 = ["mumbai","banglore","kolkata"]
cities2.pop(1)
print(cities2)

# clear()
cities2.clear()
print(cities2)

#           0       1        2        3       4       5       6       7
fruits = ["apple","mango","banana","papaya","apple","mango","grapes","apple"]

q111 = fruits.index("apple",1,5)
q11 = fruits.index("apple")
q1 = fruits.index("apple",2)
print(q1)


# reverse()
#           0        1       2       3         4
cities = ["goa","nagpur","wardha","chennai","pune"]
cities.reverse()
print(cities)

# sort()
cities.sort()
print(cities)


# append()
#            0          1           2       3
country = ["india","bangladesh","srilanka","cuba"]
country.append("pakistan")
print(country)


# insert()
country.insert(2,"china")
print(country)


# extend()

numberA = [11,22,33]
numberB  = [44,55,66]
numberB.extend(numberA)
print(numberA)
print(numberB)


animals = ["dog","lion","tiger","rabbit","snake","dog"]
q22 = animals.count("dog")
print(q22)


h = [11,22,33]
j = h.copy()
j[0] = 111
print(j)
print(h)



