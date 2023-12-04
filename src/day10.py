


# program

birthYear = [1989,1990,1991,1992]
ages = [] # [34]
# [34,33,32,31]

for x in range(len(birthYear)):
    #print(x)
    #print(birthYear[x])
    #print(2023 - birthYear[x])
    x = 2023 - birthYear[x]
    ages.append(x)

# program 2

marks = [22,33,44,66,7,8,99,44,66,77]

# for x in range(len(marks)):
#     if marks == 99:
#         print("99 available")

# for x in marks:
#     if x == 99:
#         print("99 is available")
# print(99 in marks)

# if(99 in marks):
#     print("99 available")

marks = [22,33,44,66,7,8,99,44,66,77]
above50 = []
for x in marks:
    if x > 50:
        above50.append(x)
print(above50)


# program 3
#         0  1  2  3  4  5  6  7  8  9
marks3 = [88,77,88,99,88,99,00,99,00,88]
indexOf88 = []
removeEvenIndexElement = []

for item in range(len(marks3)):
    if marks3[item] == 88:
        indexOf88.append(item)

for item in range(len(marks3)):
    if(item % 2 == 0):
        continue
    removeEvenIndexElement.append(marks3[item])
print(removeEvenIndexElement)


# program 4

#        0  1  2  3   4  5
marks = [11,22,33,44,55,66]
total = 0
total2 = 0
for item in marks:
    total = total + item
print(total)

for item in range(len(marks)):
    if item % 2 == 0 and item != 0:
        total2 = total2 + marks[item]
print(total2)





