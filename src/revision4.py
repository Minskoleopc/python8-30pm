
# intialization
#while condition:
    # statement
    # increment / decrement
# program 1
t1 = 1
while t1 <= 3:
    print(t1) # 1 # 2 # 3
    t1 = t1 + 1 # 2 # 3 # 4

# program 2
# print 1 to 5

t2 = 1
while t2 <= 5:
    print(t2)
    t2 = t2 + 1

# program 3
# print 5 to 1

t3 = 5
while t3 >= 1:
    print(t3)
    t3 = t3 - 1

# program 4
# table of 2

t4 = 2
while t4 <= 20:
    print(t4)
    t4 = t4 + 2
# program of 5 reverse
t5 = 50
while t5 >= 5:
    print(t5)
    t5 = t5 - 5
# break with while loop
t6 = 1
while t6 <= 5:
    print(t6) # 1 # 2 #3
    if t6 == 3:
        break
    t6 = t6 + 1 # 2 #3

t7 = 5
while t7 >= 1:
    if t7 == 3:
        break
    t7 = t7 -1  # 4 # 3
    print(t7)  # 4 # 3

t8 = 10
while t8 >= 5:
    if t8 == 7:
        t8 = t8 - 1 # 6
        continue
    print(t8)  # 10 # 9 # 8 # 6 # 5
    t8 = t8 - 1  # 9 # 8 # 7 # 5 # 4










