
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

# Wed , Fri
# 11 - 15 ---- 16
# 9 am (git)



















