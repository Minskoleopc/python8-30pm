

dict = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "email":"chinmaydeshpande010@gmail.com",
    "rollNo":24
}
dict2 = dict
dict2['rollNo'] = 36
print(dict2)
print(dict)

dict3 = {
    "firstName":"chinmay",
    "lastName":"dani"
}

# program 1
# copy()
dict4 = dict3.copy()
dict4['lastName'] = "deshpande"
print(dict4)
print(dict3)

# program 2
# update()
info1 = {
    "color":"red",
    "model":"q4"
}

info2 = {
    "regNo": 123
}
info2.update(info1)
print(info1)
print(info2)

# program 3
# popitem()
info3 = {
    "color":"blue",
    "mobileNumber":213,
    "city":"pune"
}
info3.popitem()
print(info3)

# program 4
# setdefault()

info4 = {
    "city":134,
    "district":34,
    "state":29
}
info4.setdefault("city","345")
print(info4)

# program 5
props = ["fn","ln","age"]
info5 = dict.fromkeys(props,0)
print(info5)
