# program 1
f1 = open('virat-kohli.png','rb')
f2 = open('virat2.png','wb')
bytes = f1.read()
f2.write(bytes)
f1.close()
f2.close()
# program 2

with open('sample.txt','w') as f:
    f.write("I am learning js \n")
    f.write("I am learning python \n")





