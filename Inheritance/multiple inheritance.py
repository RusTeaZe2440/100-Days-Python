class Employee:
    Name = "bhavesh"
    Age = 20
    Role = "Ai developer"

class Person(Employee):
    clg = "SIGCE"
    Branch = "Ai&Ml"
    

class orange(Person):
    def getinfo(self):
        print(f'''The Name of the Developer is {self.Name} and his role is {self.Role}
{self.Name} is Qualified from {self.clg} and his from batch {self.Branch} 2024.''')

o = orange()
o.getinfo()