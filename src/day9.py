
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


names = ["deepak","sameer","sham"]
names.pop()
names.pop(1)


# program 2
numbersB = [44,55,66]
numberC = numbersB
numbersB[0] = 999
print(numbersB)
print(numberC)


# program 3
numbersV = [11,22,33]
numberT  = numbersV.copy()
numberT[1] = 1111
print(numbersV)
print(numberT)


# program 4
g = [11,22,33]
h = [44,55,66]
g.extend(h)
print(g)
print(h)

# program 5
j = ["pune","mumbai","nashik","wardha"]
j.insert(2,"goa")
print(j)

# program 6

fruits = ["mango","apple","chikoo"]
fruits.append("papaya")
print(fruits)
#["mango","apple","chikoo","papaya"]

fruits.sort()
print(fruits)
#["apple","chikoo","mango","papaya"]

fruits.reverse()
#["papaya","mango","chikoo","apple"]

numbers  = [11,22,33,44,55,44]
q2 = numbers.count(44)
print(q2)

for x in range(len(numbers)):
    print(x)
    print(numbers[x])













