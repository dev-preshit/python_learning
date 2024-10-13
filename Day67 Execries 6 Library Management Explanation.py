#EXECRIES 6
#Library Management System
#Write a Library class with no_of_books and books as two instance variables. Write a program to create
# a library from this Library class and show how you can print all books, add a book and get the number
# of books using different methods. Show that your program doesnt persist the books after the program
# is stopped!
"""
    In this exercise, we created a Library Management System using a Python class. The goal is to provide basic functionalities for managing a collection of books, including:

    • Adding books to the library.
    • Displaying the total number of books.
    • Listing all the books currently in the library.

    The system also demonstrates that the books are not persisted after the program ends.
Explanation:

    Class Definition: We define a class called Library which contains two instance variables:
        • no_of_books: An integer to keep track of the total number of books.
        • books: A list to store the names of the books.

    Class Methods:

        • add(): This function allows the user to add a book to the library. It takes the book's name as input from the user, appends it to the books list, and increments the no_of_books by 1.

        • show(): This function prints all the books in the library. If there are no books, it simply informs the user that the library is empty.

        • no_of_book(): This function displays the total number of books currently in the library.

    Main Program:
        We instantiate the Library class and store it in a variable called name.
        A loop is used to keep prompting the user for actions, which are:
            1: Add a book.
            2: Display the total number of books.
            3: Show the list of books in the library.
            0: Exit the program.
        The input handling is wrapped in a try-except block to catch any invalid inputs.    
"""
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