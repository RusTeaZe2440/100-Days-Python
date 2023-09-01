class Employee:
    
    role = "developer"

class programmer(Employee):
    def getinfo(self):
        print(f"the employee role is {self.role}")

e = Employee()
p = programmer()
p.getinfo()
