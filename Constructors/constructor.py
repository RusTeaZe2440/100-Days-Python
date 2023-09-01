class employee():
    Id = 45
    Name = "bhavesh"
    def info(self):
        print(f"{self.Id} is a id of {self.Name}")

a = employee()
a.Id = 96  # it will overwrite the id of 45
a.info()


# parameterized constructors 
# is the constructor that has been given parameters

class details():
    def __init__(self,animal,group):
        self.name = animal
        self.group = group
    def info(self):
        print(f"{self.name} belongs to the group of {self.group}")

a = details("Leopard","Mammals")
print(a.name ,"belongs to group of", a.group)

# default constructor

class animaldetails():
    def __init__(self):
        print("lion is animal which belongs to mammal group")
    
b = animaldetails()

