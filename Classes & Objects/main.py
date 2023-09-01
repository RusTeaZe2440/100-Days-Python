class person():
    Name = "bhavesh"
    Age = 20
    role = "Ai developer"
    def info(self):
        print(f"{self.Name} is a {self.role}")

a = person()
# overrinting the name and role
a.Name = "john"
a.role = "software developer developer"

a.info()