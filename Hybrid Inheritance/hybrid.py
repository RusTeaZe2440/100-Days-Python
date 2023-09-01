class vehicle:
    def show(self,Fueltype):
        self.Fuel = Fueltype
        print(f"FuelType: {self.Fuel}")

class car(vehicle):
    def c1(self,wheels):
        self.wheels = wheels
        print(f"wheels:{self.wheels}")

class Racing(vehicle):
    def r1(self,Type):
        self.type = Type
        print(f"Type: {self.type}")

class Ferrari(car,Racing):
    def modeltype(self,model):
        self.model = model 
        print(f"Model Name = {self.model}")

fer = Ferrari()
fer.show("pertrol")
fer.r1("Formula One")
fer.modeltype("Ferrari X78")