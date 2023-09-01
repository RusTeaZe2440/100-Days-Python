class Employee:
    def __init__(self):
        self.__name = "bhavesh" # simply use __ before the variable 
        self.age = 20

a = Employee()
print(a._Employee__name)  # if you want to access the variable (_Employee__name)


# name mangling

class person():
    def __init__(self):
        self._private_attribute = "i am private attribute"
        self.__mangledattribute = "i am mangled attribute"

p = person()
print(p._private_attribute)
print(p._person__mangledattribute)