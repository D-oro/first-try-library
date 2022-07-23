from models.book import *

book1 = Book("Talk to your duck - an Introduction to Coding", "Ducky McDuck", "How-to guides")
book2 = Book("The Mousetrap", "Kat Kitten", "Mystery")
book3 = Book("The Chicken or the Egg", "Hen Rooster", "Autobiography")
books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def remove_book(book):
    books.pop(book)