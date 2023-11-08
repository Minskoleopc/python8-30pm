
for x in range(1,10):
    print(x)

for x in range(2,22,2):
    print(x)

for x in range(5,0,-1):
    print(x)

for x in range(50,0,-5):
    print(x)

for x in range(1,10):
    if x == 3:
        break
    print(x)

for x in range(2,22,2):
    print(x)
    if x == 14:
        break

# continue with  for

for x in range(1,6):
    if x == 3:
        continue
    print(x) # 1 # 2 # 4 # 5


for x in range(20,2,-2):
    if x == 14:
        continue
    print(x)


# intialization
# while(condition):
    # statement
    # increment / decrement


t1 = 1
while t1 <= 5:
    print(t1) # 1 # 2 # 3 # 4 # 5
    t1 = t1 + 1 # 2 # 3 # 4 # 5 # 6

t2 = 5
while t2 >= 1:
    print(t2)  # 5  # 4 # 3 # 2 # 1
    t2 = t2 - 1  # 4 # 3 # 2 # 1  # 0

t3 = 1
while t3 <= 3:
    print("hello") # "hello" # "hello" # "hello"
    t3 = t3 + 1  # 2 # 3 # 4

t4 = 2
while t4 <= 20:
    print(t4)
    t4 = t4 + 2

t5 = 50
while t5 >= 5:
    print(t5)
    t5 = t5 - 5


# break with while

# intialization
#while(condition):
    # statement
    # increment / decrement


# program 2

g1 = 1
while g1 < 5:
    print(g1) # 1 # 2 # 3 # 4
    g1 = g1 + 1 # 2 # 3 # 4 # 5

# program 3
g2 = 1
while g2 <= 5:
    if(g2 == 3):
        break
    print(g2) #1 # 2
    g2 = g2 + 1 # 2 # 3

# program 4
g3 = 2
while(g3 <= 20):
    print(g3) # 2 # ------- 14
    if g3 == 14:
        break
    g3 = g3 + 2 # 4

# program 5
g3 = 2
while(g3 <= 20):
    if g3 == 14:
        break
    print(g3)
    g3 = g3 + 2

# program 6
g4 = 6
while(g4 >= 1):
    print(g4) #6 # 5 # 4 # 3
    if g4 == 3:
        break
    g4 = g4 - 1 # 5 # 4 # 3

# program 7
# contine with while

g5 = 1
while g5 <= 5:
    if g5 == 3:
        g5 = g5 + 1 # 4
        continue
    print(g5) # 1 # 2 # 4 # 5
    g5 = g5 + 1 # 2 # 3 # 4 # 6



























