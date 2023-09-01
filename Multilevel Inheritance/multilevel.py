class Employee:
    def show(self,name , e_id):
        self.name = name
        self.e_id = e_id
        print(f"the name is {self.name} and id is {self.e_id}")

class Programmer(Employee):
    
    def show_details(self,age,role):
        self.Age = age
        self.role = role
        print(f"The age is {self.Age} and his role is {self.role} ")

        
class Person(Programmer):
    
    def details(self,mail_id,mob_no):
        self.mail_id = mail_id
        self.mob_no = mob_no
        print(f"Mail_id = {self.mail_id}")
        print(f"Mob_no : {self.mob_no}")

P = Person()
P.details("bhaveshbhalerao98@gmail.com",9930061620)
P.show_details(20,'Ai Developer')
P.show("bhavesh",25)