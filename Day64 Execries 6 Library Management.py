#EXECRIES 6
#Library Management System
#Write a Library class with no_of_books and books as two instance variables. Write a program to create
# a library from this Library class and show how you can print all books, add a book and get the number
# of books using different methods. Show that your program doesnt persist the books after the program
# is stopped!

class Library:
    def __init__(self) -> None:
        self.no_of_books = 0
        self.books = []

    def add(self):
        book = input('Enter book name: ')
        self.books.append(book)
        self.no_of_books += 1

    def show(self):
        print("you have following books:")
        for index,book in enumerate(self.books,start = 1 ):
            print(f"{index}.{book}")
        

    def no_of_book(self):
        print(f"You have {self.no_of_books} in total")

name = Library()
command = 4
try:
    command = int(input("Enter what you want to do \n 1 for add books \n 2 for number of books \n 3 for for show how many books \n 0 for exit\n==>"))
except Exception as e:
    print(e)
while command in [1,2,3,0,4]:
    match command:
        case 1:
            name.add()
        case 2:
            name.no_of_book()
        case 3:
            name.show()
        case 0:
            break
    try:            
        command = int(input("\nEnter what you want to do \n 1 for add books \t 2 for number of books \n 3 for for show how many books \n 0 for exit\n==>"))
    except Exception as e:
            print(e)
    if(command != 0):
        continue

