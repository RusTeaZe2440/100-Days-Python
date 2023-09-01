x = [2,2,523,2]
print(dir(x))

#output
# # '__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__
# ', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '
# __init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex
# __', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '
# append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


class person:
    def emp1(self,name,age):
        self.name = name 
        self.age = age
        # print(f"the name is {self.name} and age is {self.age}")
p = person()
# p.emp1("bhavesh",20)
p.__dict__
# output
# {'name': 'John', 'age': 30}


x = [2,2,523,2]
print(dir(x))

help(p)
# class person(builtins.object)
#  |  Methods defined here:
#  |
#  |  emp1(self, name, age)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
# -- More  --