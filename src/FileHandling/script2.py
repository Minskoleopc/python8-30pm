# number of lines , number of characters , number of words
import os, sys
fname = input("Enter the fname:")
if os.path.isfile(fname):
    f = open(fname,'a+')
    # f.write("I am learning py"+"\n")
    # f.write("I am learning js" + "\n")
    # f.write("I am learning sql" + "\n")
    # f.write("I am learning ruby" + "\n")
else:
    print("file not found")
    sys.exit()
f.seek(0,0)
cl = 0
cw = 0
cc = 0

for line in f:
    words = line.split(" ")
    cl = cl + 1
    cw = cw + len(words)
    cc = cc + len(line)
    #"".join(line.split(" "))
print(cl)
print(cw)
print(cc)
f.close()

#"I am learning js".split(" ") ==> ["I","am","learning","js"]
