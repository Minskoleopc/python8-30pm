

# one input and multiple outcome
# numT > 0  and numT <= 5   -----> 10 % discount
# numT > 5  and numT <= 10  -----> 20 % discount
# numT > 10                 -----> 30 % discount

# program 1
numT = 7
if numT > 0 and numT <= 5:
    print("10 % discount")
if numT > 5 and numT <= 10:
    print("20 % discount")
if numT > 30:
    print("30 % discount")

# program 2
numT = -17

if numT > 0 and numT <= 5:
    print("10 % discount")
elif numT > 5 and numT <= 10:
    print("20 % discount")
elif numT > 10:
    print("30 % discount")
else:
    print("Invalid input")


# program 3
marks = 92
if marks >= 90:
    print("Grade A")
if marks >= 75:
    print("Grade B")
if marks >= 65:
    print("Grade C")

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 65:
    print("Grade C")
else:
    print("Try again")

# program 4

s = 10
t = 5

if s > t:
    print("s is greater")
else:
    print("t is greater")


# program 5
x1 = 10
x2  = 60
x3 = 300

if x1 > x2 and x1 > x3:
    print("x1 is greater")
elif x2 > x3 and x2 > x1:
    print("x2 is greater")
else:
    print("x3 is greater")

# program 6
q = 100
r = 5
if q > r :
    print("q is greater")
else:
    print("r is greater")

print("q is greater") if q > r else print("r is greater")


age = 17
q2 = "can drive" if age >= 18 else "cannot drive"
print(q2)


























