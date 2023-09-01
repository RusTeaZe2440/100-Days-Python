# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat

class animal:
    def __init__(self,name,aclass):
        self.name = name
        self.aclass = aclass

    def acat(self):
        print("The cat says meow meow")

class cat(animal):
    def showdetails(self):
        print(f"the name of the animal is {self.name} and belongs to class {self.aclass}")


c = cat("cat",'domestic animal')
c.showdetails()
c.acat()