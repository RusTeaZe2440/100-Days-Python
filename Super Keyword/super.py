class Employee:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

class Programmer(Employee):
    def child(self,name,age, lang):
        super().__init__(name, age)
        self.lang = lang
        print(f"The name of the programmer {self.name} and his age is {self.age} he works on {self.lang}")

e = Employee("Rohan" ,34)
p = Programmer("bhavesh",20)
p.child("bhavesh",20,"Python")
