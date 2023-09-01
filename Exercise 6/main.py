class Library:

    def __init__(self,listofbooks):
        self.books = listofbooks

    def displayAvailableBook(self):
        print("The List Of Available Books are... ")
        for book in self.books:
            print("*",book)

    def borrowbook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry the book you entered is not available")
            return False

    def returnbook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the book have a good day")


class Student:

    def requestbook(self,bookName):
        self.book = input("Enter the name of the book: ").lower()
        return self.book
    def returnbook(self):
        self.book = input("Enter name of the book that you want to return: ").lower()
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Hands On ML","Python","DSA","Computer Network"])
    Students = Student()

    while(True):
        welcomemsg = '''======= Welcome to Library ========= \n
        Please choose the option 
        1. List of booksAvailable
        2. RequestBook
        3. ReturnBook
        4. Exit the Library

        '''
        print(welcomemsg)
        a = int(input("Enter the choice:"))

        if a==1:
            centralLibrary.displayAvailableBook()
        elif a==2:
            centralLibrary.borrowbook(Student.requestbook())
        elif a==3:
            centralLibrary.returnbook(Student.returnbook())
        else:
            exit()