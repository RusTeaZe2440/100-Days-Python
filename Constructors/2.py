class Employee:
    def __init__(self,arole,aname):
        self.role = arole
        self.name = aname
        print(f"The role is {self.role} and his name is {self.name}")

b = Employee("ai","bhavesh")


# instance and class variable 
class Employee:    # employee is a class
    no_of_employee = 5

bhavesh = Employee()   #bhavesh is an object

bhavesh.name = "bhavesh"  #name is a instance 
bhavesh.role = "Ai"   #role is an instance 
bhavesh.age = 20    #age is an instance
Employee.no_of_employee = 7
print(Employee.no_of_employee)

