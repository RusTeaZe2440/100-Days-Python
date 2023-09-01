# dictionary uses several built in methods such as update()

dic = {
    "name": "bhavesh",
    "Age": 20,
    "Role": "ai&Ml"
}

dic.update({"Age": 21})
print(dic)

# dictionary uses clear method that we can use to remove item from dictionary

dic = {
    "name": "bhavesh",
    "Age": 20,
    "Role": "ai&Ml"
}

dic.clear()
print(dic)
# it will display {}

# pop() method is used to remove item from the dictionary

dic = {
    "name": "bhavesh",
    "Age": 20,
    "Role": "ai&Ml"
}

dic.pop("Age")  # it takes only one key-value pair
print(dic)


# popitem() it is used to remove last key-value pair in the dictionary

dic = {
    "name": "bhavesh",
    "Age": 20,
    "Role": "ai&Ml"
}

dic.popitem()
print(dic)

# del keyword is used to completely deletes variable or key-value pair

dic = {
    "name":"bhavesh",
    "Age":20,
    "Role" : "ai&Ml"
}

del dic
print(dic)

# deleting key value pair

dic = {
    "name":"bhavesh",
    "Age":20,
    "Role" : "ai&Ml"
}

del dic["name"]

print(dic)


