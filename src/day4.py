# conditional statements
# one input and multiple outcome
# concert

# numT > 0 and numT <= 5  ----->   5 % discount
# numT > 5 and numT <= 10 ----->   10 % discount
# numT . 10               ----->   20 % discount

# discount
# flat 100 rs off
# percentage 10 %
# range discount - 2-5 , 5- 10
# special discount -  coupon

#if(condition):
    # statement

# program 1
numT = 17
if numT > 0 and numT <= 5:
    print("5 % discount")
if numT > 5 and numT <= 10:
    print("10 % discount")
if numT >10:
    print("20% discount")

# program 2
#if elif

numT2 = -17

if numT2 > 0 and numT2 <= 5:
    print("5 % discount")
elif numT2 > 5 and numT2 <= 10:
    print("10 % discount")
elif (numT2 > 10):
    print("30 % discount")
else:
    print("Invalid input")

# program 3

marks = 44
#
# if marks >= 90:
#     print("Grade A")
# if marks >= 75:
#     print("Grade B")
# if marks >= 65:
#     print("Grade C")

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 65:
    print("Grade C")
else:
    print("Try again")


# program 4
s  = 10
t = 50

if s > t:
    print("s is greater")
else:
    print("t is greater")


# tenary operator
print("s is greater") if s > t else print("t is greater")









