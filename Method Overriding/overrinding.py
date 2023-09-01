class animal:

    def runnning(self): # overriden method
        print("This is parent class who is running")


class lion(animal):

    def running(self):
        print("This is child class ")  # this method overides parent class method running

l = lion()
l.running()


# Python program to demonstrate
# overriding in multiple inheritance


# Defining parent class 1
class Parent1():
		
	# Parent's show method
	def show(self):
		print("Inside Parent1")
		
# Defining Parent class 2
class Parent2():
		
	# Parent's show method
	def display(self):
		print("Inside Parent2")
		
		
# Defining child class
class Child(Parent1, Parent2):
		
	# Child's show method
	def show(self):
		print("Inside Child")
	
		
# Driver's code
obj = Child()

obj.show()
obj.display()



# Python program to demonstrate
# overriding in multilevel inheritance


class Parent():
		
	# Parent's show method
	def display(self):
		print("Inside Parent")
	
	
# Inherited or Sub class (Note Parent in bracket)
class Child(Parent):
		
	# Child's show method
	def show(self):
		print("Inside Child")
	
# Inherited or Sub class (Note Child in bracket)
class GrandChild(Child):
		
	# Child's show method
	def show(self):
		print("Inside GrandChild")		
	
# Driver code
g = GrandChild()
g.show()
g.display()


# Python program to demonstrate
# calling the parent's class method
# inside the overridden method using
# super()


class Parent():
	
	def show(self):
		print("Inside Parent")
		
class Child(Parent):
	
	def show(self):
		
		# Calling the parent's class
		# method
		super().show()
		print("Inside Child")
		
# Driver's code
obj = Child()
obj.show()
