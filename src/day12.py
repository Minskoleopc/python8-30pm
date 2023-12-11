
# program1
birthYear = [1989,1990,1991,1992]
#[34,33,32,31]
a = []
for item in birthYear:
    a.append(2023 - item)
print(a)

#[expression:loop:condition]
b = [2023 - item for item in birthYear]
print(a)

# program2
numberB = [1,2,3,4,5,6,7,8,9,10]
c = [item * 2 for item in numberB]
print(c)

# program3
marks = [22,33,44,11,22,33,44,56,77,22,34]
b = []
for item in marks:
    if item > 40:
        b.append(item)
print(b)
c = [item for item in marks if item > 40]
print(c)

c = [item for item in range(len(marks)) if marks[item] > 40]
print(c)

# program 4
names = ["chinmay","shirish","ram","sharddha","samay"]
d = [item[0] for item in names ]
print(d)


s = 1
v = 5
if s > v:
    print("s is greater")
else:
    print("v is greater")
print("s is greater") if s > v else print("v is greater")

# program 5
h1 = [1,3,4,55,22,33,44,55,66,777,88,99,44,33]
a1 = []
for item in h1:
    if item % 2 == 0:
        a1.append("even")
    else:
        a1.append("odd")
print(a1)
h2 = ["even" if item % 2 == 0 else "odd" for item in h1]
print(h2)
listA = [1,2,3]
listB = [4,5,6]
#[4,10,18]
sum = []
for item in range(len(listA)):
    sum.append(listA[item]*listB[item])
print(sum)
f = [listA[item] * listB[item] for item in range(len(listA))]
print(f)



























