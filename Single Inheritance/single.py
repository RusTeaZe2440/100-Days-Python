class Animal:
    def __init__(self, name , aclass):
        self.name = name 
        self.aclass = aclass


class name(Animal):
    
    def show(self):
        print(f"The name of the animal is {self.name} and it belongs to {self.aclass}")

na = name('tiger','wild')
na.show()