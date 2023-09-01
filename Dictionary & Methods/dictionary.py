dic = {
    "name":"bhavesh",
    "Age":20,
    "Role" : "ai&Ml"
}
print(type(dic))
print(dic)


# accessing dic single values  using either square brackets or using get method 


dic = {
    "name":"bhavesh",
    "Age":20,
    "Role" : "ai&Ml"
}

print(dic.get("Role"))

# Accessing multiple values using value() method 

dic = {
    "name":"bhavesh",
    "Age":20,
    "Role" : "ai&Ml"
}

r = dic.values()
print(r)

# accessing keys in dictionaries
dic = {
    "name":"bhavesh",
    "Age":20,
    "Role" : "ai&Ml"
}

print(dic.keys())

# accessing key values pair usilng item methods

dic = {
    "name":"bhavesh",
    "Age":20,
    "Role" : "ai&Ml"
}

print(dic.items())
