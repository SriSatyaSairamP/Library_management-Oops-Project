## 12-05-2026

## Library_Management-Oops-Project

from abc import ABC,abstractmethod

class Book:

    def __init__(self,title,author):
        self.title=title
        self.author=author

    def display(self):
        print(f"Book: {self.title}")
        print(f"Author: {self.author}")

class Member(ABC):

    def __init__(self,name):
        self.name=name
        self.borrowed_books=[]

    @abstractmethod
    def calculate_fine(self,days):
        pass

    def show_books(self):

        print(f"\n{self.name} borrowed books")

        if not self.borrowed_books:
            print("No books borrowed")
            return
        else:
            for book in self.borrowed_books:
                print(book.title)

class Student(Member):

    def calculate_fine(self,days):

        if days<=7:
            return 0
        return (days-7)*20
class Teacher(Member):

    def calculate_fine(self,days):

        if days<=14:
            return 0
        return (days-14)*10


class Library:

    def __init__(self,name):

        self.name=name
        self.books={}

    def add_book(self,book,copies):

        if book in self.books:
            self.books[book]+=copies
            print(f"{copies} more copies of {book.title} added")
        else:
            self.books[book]=copies
            print(f"{book.title} added to library with {copies} copies")

    def show_books(self):

        print(f"\nLibrary: {self.name}")

        if not self.books:
            print("No Books Avaliable")
        else:
            for book,copies in self.books.items():
                print(f"\nBook: {book.title}")
                print(f"Author: {book.author}")
                print(f"Copies: {copies}")

    def borrow_book(self,member,book):

        if book not in self.books:
            print("Book not found")
            return
        if self.books[book]<=0:
            print("No copies available")
            return

        if book in member.borrowed_books:
            print(f"{member.name} already borrowed {book.title}")
            return

        member.borrowed_books.append(book)
        self.books[book]-=1

        print(f"{member.name} borrowed {book.title}")

    def return_book(self,member,book):

        if book not in member.borrowed_books:
            print(f"{book.title} is not borrowed by {member.name}")
            return

        member.borrowed_books.remove(book)
        self.books[book]+=1
        print(f"{member.name} returned {book.title}")

book1=Book("Python Basics","Ravi Kumar")
book2=Book("OOP Concepts","Ram Sharma")
book3=Book("Data Structures","Narasimha Rao")

book1.display()

student1=Student("Ish@@n")
student2=Student("Sairam")

teacher1=Teacher("Prakash")
teacher2=Teacher("Sreedhar")

library=Library("Society Library")
library.add_book(book1,2)
library.add_book(book2,5)
library.add_book(book1,3)
library.add_book(book2,1)

library.show_books()

library.borrow_book(student1,book1)
library.borrow_book(teacher1,book2)

teacher1.show_books()

library.return_book(student2,book1)
library.return_book(student1,book1)

library.show_books()

print(f"\nStudent Fine: ₹{student1.calculate_fine(10)}")












