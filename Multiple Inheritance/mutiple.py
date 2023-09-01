class Employee:
    def __init__(self,name):
        self.name = name
    def show(self):

        print(f"The marks obtained are {self.name}")
class Cricketer:
    def __init(self,Cricket):
        self.cricket = Cricket

    def show(self):
        print(f"The role of the crickter is {self.cricket}")
    
class Topper:
    def __init(self,percentage):
        self.percentage = percentage

    def show(self):
        print(f"The marks obtained are {self.percentage}")

class boy(Cricketer,Employee,Topper):
    def __init__(self,Cricket,name,percentage):
        self.cricket = Cricket
        self.name = name
        self.percentage = percentage


b = boy("batsman","bhavesh",82)
b.show()  # it will display cricketer show method bcoz we have written it first in boy class
