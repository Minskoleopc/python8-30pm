# program 1
# open the file for writing data
# f = open("myfile.txt",'w')
# # enter the characters from keyword
# e = input('Enter the name')
# # write the string into the file
# f.write(e)
# # closing th file
# f.close()


# program 2
# f = open('myfile.txt','r')
# str = f.read()
# print(str)
# f.close()


# program 3
# f = open('myfile.txt','w')
# print("Enter '@' to exit")
# while str != '@':
#     str = input("Please enter multiple names")
#     if str != '@':
#         f.write(str + "\n")
# f.close()

# program 4
# f = open('myfile.txt','+a')
# print("Enter '@' to exit")
# while str != '@':
#     str = input("Please enter multiple names")
#     if str != '@':
#         f.write(str + "\n")
# f.seek(0,0)
# str = f.read()
# print(str)
# f.close()

# program 1
# writing to the file
# f  = open("myfile2.txt","w")
# str = input("Enter the name")
# f.write(str)
# f.close()

# program 2
# f  = open("myfile2.txt","r")
# e = f.read()
# print(e)
# f.close()


# program 3
# f = open('myfile2.txt','a+')
# print("Enter '@' to exist")
# while str != "@":
#     str = input("Enter the name")
#     if str != "@":
#         f.write(str + "\n")
# f.close()

# program 4
# f = open('myfile3.txt','a+')
# print("Enter '@' to exist")
# while str != "@":
#     str = input("Enter the name")
#     if str != "@":
#         f.write(str + "\n")
# f.seek(0,0)
# # f.seek("offset","fromwhere")
# # f.seek(10,0) # 10 bytes from start of the file
# # f.seek(10,1) # 10 bytes from currect position
# # f.seek(10,2) # 10 bytes starting from last
# q = f.read()
# print(q)
# f.close()

#
import  os ,sys
print(os.path)
fname = input("Enter the filename: ")

if os.path.isfile(fname):
    f = open(fname,"r")
else:
    sys.exit()
i = f.read()
print(i)
f.close()


