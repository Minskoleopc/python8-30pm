

# list
# string
# dictionary
# tuple
# set
# program 1

numbers = [11,22,33]
print(numbers[0])
print(type(numbers))

#           0         1         2        3       4
names = ["chinmay","sarika","poorva","mayuri","amol"]
print(names)
print(names[0])
print(names[4])

# mixed
mixedArray = ["chinmay","deshpande",7709192441,True]

# list

#           0        1        2         3
cities = ["pune","bangalore","jaipur","nagpur"]
q1 = len(cities)
print(q1)
print(type(q1))

# retrive
print(cities[0])

# update
cities[0] = "wardha"
print(cities)

#add
cities.append("goa")
print(cities)

#delete
#cities.pop()
# ['wardha', 'bangalore', 'jaipur', 'nagpur', 'goa']
cities.pop(2)
print(cities)
cities.remove("nagpur")
print(cities)


# loop
i = 2
print(i)
print(type(i))

h = "chinmay"
print(h)
print(type(h))

y = True
print(y)
print(type(y))

flowers = ["lily",'jasmine','rose']
print(flowers)
print(type(flowers))

w1 = len(flowers)
print(w1)
print(type(w1))

fruits = ["apple","mango","banana","papaya"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# element available or not available
print("apple" in fruits)
print("Apple" in fruits)

if "Apple" in fruits:
    print("fruit available")
else:
    print("fruit not available")








