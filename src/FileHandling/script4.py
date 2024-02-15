# chinmay mayuri sarika
# 'chinmay   '
# 'mayuri    '
# 'sarika    '


#reclen = 10

# with open('cities.bin',"wb") as f:
#     n = int(input("enter the number of users"))
#     for i in range(n):
#         name = input("enter the name") #"chinmay"
#         name = name + (reclen - len(name)) * ' '
#         name  = name.encode()
#         f.write(name)


# program 2
# reclen = 10
# with open('cities.bin','rb') as f:
#     n = int(input("which record to read ?")) # 3
#     f.seek(reclen * (n-1))
#     str = f.read(reclen)
#     str = str.decode()
#     print(str)


# program 3 -----> search the name in the file
# import os
# reclen = 10
# size = os.path.getsize('cities.bin') # 30
# n = int(size/reclen) # 30/10 --- 3
# with open('cities.bin','rb') as f:
#     name = input('enter the name') #"ram" # "ram          "
#     name = name.encode()
#     position = 0
#     found = False
#
#     for x in range(n):
#         f.seek(position)
#         str = f.read(reclen) #"ram          "
#         if name in str:
#             found = True
#         position = position + reclen
#     if found:
#         print("user available")
#     else:
#         print("user not available")


#ram       tanmay   sham

import os
reclen = 10

size  = os.path.getsize('cities.bin') # 30
n = int(size/reclen) # 3
with open("cities.bin" , "r+b") as f:
    newname  = input("Enter the name") #tanmay
    replace =  input("Name to replace") #chinmay
    newname = newname + (reclen - len(newname)) * " "
    replace = replace + (reclen - len(replace)) * " "
    newname = newname.encode()
    replace = replace.encode()
    position = 0
    found = False
    for x in range(n):
        f.seek(position)
        str = f.read(reclen)
        print(str)
        print(replace)
        if str == replace:
            found = True
            break
        else:
            position = position + reclen

    if found:
            f.seek(-10,1)
            f.write(newname)
            print("city successfully replaced")
    else:
            print("city not found")
            # 0 - start of file
            # 1 - current position
            # 2 - end of file


































# program 4 -----> search and modify the record

# program 5 -----> search and delete the record













