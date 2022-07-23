from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book, remove_book
from models.book import Book

@app.route('/library')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/library/show')
def show():
    return render_template('show.html', title='Show', books=books)

@app.route('/library/new')
def new():
    return render_template('new.html', title='New', books=books)

@app.route('/addbook', methods=['POST'])
def addbook():
    bookTitle = request.form['title']
    bookAuthor = request.form['author']
    bookGenre = request.form['genre']
    newBook = Book(title=bookTitle, author=bookAuthor, genre=bookGenre)
    add_new_book(newBook)
    return redirect('/library')

@app.route('/removebook/', methods = ['POST'])
def remove_book(book):
    remove_book(book)
    return redirect('/library')

