# # variables
# # arithmetic
# # conditional
# # types
# # comparision
# # logical
# # loops
# # break and continue
# # list
# # list comprehension
# # dictionary
# # string
#
# # string
# x = "hello"
# y  = 'chinmay'
# print(x)
# print(y)
# print(' The quote is "Try try but do not cry" ')
# print(" This is chinmay's book  ")
# a = """
#     I am learning javascript and python
#     I find them 90 % similar
#     "hello"
#     'bye'
#
# """
# b = '''
#     I am learning javascript and python
#     I find them 90 % similar
#     "hello"
#     'bye'
# '''
# # learning
# """
#     This is multiline comment
# """
#
# # program 2
# # String stotes the value by index ??
# first_name = "chinmay"
# print(first_name)
# print(type(first_name))
# print(first_name[0])
#
#
# last_name  = "deshpande"
# # 0  1  2  3  4  5  6  7  8
# # d  e  s  h  p  a  n  d  e
# #-9                     -1
# print(last_name[0])
# print(last_name[-1])
#
# # for loop
#
# #range
# for i in range(len(last_name)):
#     #print(i)
#     print(last_name[i])
#
# # without range
# for char in first_name:
#     print(char)
#
# # while
# i1 = 0
# while(i1 < len(last_name)):
#     #print(i1)
#     print(last_name[i1])
#     i1 = i1 + 1
#
# # ------ methods --------------
# # program 1
# first_name = "chinmay"
# print(type(first_name))
# fn = first_name.upper()
# print(fn)
#
# # program 2
# lastName = "Deshpande"
# ln = lastName.lower()
# print(ln)
#
# # Slicing
# city  = "chandrapur"
# # 0   1   2   3   4   5   6   7    8    9
# # c   h   a   n   d   r   a   p    u    r
# # -10 -9  -8  -7  -6  -5  -4  -3   -2   -1
# #city[startIndex:endIndex:steps]
# print(city[1:])
# print(city[3:9])
# print(city[3:-2])
# print(city[-7:7])
# print(city[:7])
# print(city[:-7])
# print(city[-10 :-7])
# print(city[-1 :-3])
# # 0   1   2   3   4   5   6   7    8    9
# # c   h   a   n   d   r   a   p    u    r
# # -10 -9  -8  -7  -6  -5  -4  -3   -2   -1
# print(city[0:9:1])
# print(city[::-1])
#
# # program 4
# city2 = "apple"
# q1 = city2.count("p")
# print(q1)
#
# city3 = "chandrapura"
# q2 = city3.count("a",4)
# print(q2)
#
# city3 = "chandrapur"
# q2 = city3.count("a",4,8)
# print(q2)
#
# # program5
# city5 = "wardha"
# q3 = city5.capitalize()
# print(q3)
#
# #program 6
# info = "chinmay deshpande 7709192441"
# email = "chinmaydeshpande@gmail.com"
# # ["chinmay","deshpande","7709192441"]
# q4 = info.split("a")
# print(q4)
# q5 = email.split("@")
# username = q5[0]
# print(username)


# program 7
str1 = "chinmay"
str2 = "deshpande"
print(str1 + str2)


# program 8
name = "chinmay deshpande"
age = 34
# My name is chinmay deshpande and age is 34
uinfo = "My name is {} and age is {}".format(name,age)
print(uinfo)
# alternative method
print(f"My name is {name} and age is {age}")

# program 9
info2 = "i am learning javascript"
info3 = info2.replace("javascript","python")
print(info3)

# program10
fruit = "apple"
info4 = fruit.startswith("a")
info5 = fruit.startswith("App")
print(info4)
print(info5)

# program 11
fruit = "papaya"
info6 = fruit.endswith("ya")
info7 = fruit.endswith("a")
print(info6)
print(info7)

# program 12
city = " goa "
# print(len(city))
# print(len(city.strip()))

info8 = city.lstrip()
x = len(info8)
print(x)

info9 = city.rstrip()
x = len(info9)
print(x)

# program 13
#                    0      1      2     3
city = "pune"   #    p      u      n     e
print(city.index("n"))
print(city.index("p"))

# program 14
listA = [11,22,33,44,55,66]
listA[0] = 111
print(listA)

#
# h = "Hello"
# h[0] = "H"

# program 15
info9 = "chinmay".isalpha()
print(info9)
info10 = "12414344345".isdigit()
print(info10)

print("32423@".isalnum())










