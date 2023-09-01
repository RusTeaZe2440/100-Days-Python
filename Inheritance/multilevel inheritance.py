class person:
    def info(self):
        self.name = 'bhavesh'
        self.age = 20

    def getinfo(self):
        print(f"The name of the person is {self.name} and his age is {self.age}")

p = person
p.getinfo()