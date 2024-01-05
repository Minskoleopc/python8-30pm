
# program 1
setA  = {11,22,33,44}
setA.pop()
print(setA)

# program 2
setA  = {11,22,33,44}
setA.update([55,66,77])
setA.update((88,99,100))
setA.update({101,102,103})
print(setA)

# program 3
setC = {11,22,33}
setD = {22,33,44}
setE = setC.intersection(setD)
print(setE)

# program 4
setC = {11,22,33}
setD = {22,33,44}
setF = setC.union(setD)
print(setF)

# program 5
setC = {11,22,33}
setD = {22,33,44}
setC.intersection_update(setD)
print(setC)

# program 6
setC = {11,22,33}
setD = {22,33,44}
print(setC.difference(setD))
print(setD.difference(setC))

# program 7
setC = {11,22,33}
setD = {22,33,44}
setC.difference_update(setD)
print(setC)
setC = {11,22,33}
setD = {22,33,44}

#setC.intersection(setD) 22,33
#setC.difference(setD) 11
#setC.union(setD) 11,22,33,44
#setC.intersection_update(setD) 22,33
#setD.intersection_update(setC) 22,33
#setD.difference(setC) // 44
#setD.difference_update(setC) // 44

# program 8
setC = {11,22,33}
setD = {22,33,44}
setJ = setC.symmetric_difference(setD)
print(setJ)

setC.symmetric_difference_update(setD)
print(setC)

# program 9
setC = {11,22}
setD = {11,22,33,44}
print(setC.issubset(setD))
print(setD.issuperset(setC))

# program 10
setC = {112,222}
setD = {11,22,33,44}
print(setC.isdisjoint(setD))

# program 11
setC = {112,222}
setD = {11,22,33,44}

setC.remove(112)
print(setC)

print(setC.discard(112))
setCities = {"pune","mumbai","banglore","kolkata"}
print(setCities)
for item in setCities:
    print(item)