class Employee:
    company_name = "Apple"

    def showw(self):
        print(f"the name of the company is {self.company_name}")
    @classmethod #it will directly change class attribute
    def changecompany(self,company):
        self.company_name = company
e1 = Employee()
e1.changecompany("Microsoft")  #using this we will change company name using classmethod above the function
e1.showw()
