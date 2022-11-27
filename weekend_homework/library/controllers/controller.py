from flask import render_template, request, redirect
from models.books import books, get_book, add_book, delete_book, update_stock
from models.book import Book
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def list_books():
    return render_template('books.html', books=books)

@app.route('/books/<int:book_index>')
def find_book(book_index):
    my_book = get_book(book_index)
    return render_template('book.html', book=my_book)

@app.route('/books/new')
def new_book():
    return render_template('add_book.html')

@app.route('/books', methods=['POST'])
def save_book():
    form_data = request.form
    book_title = form_data["book_title"]
    book_author = form_data["book_author"]
    book_genre = form_data["book_genre"]
    checked_in = 'checked_in' in form_data
    new_book = Book(book_title, book_author, book_genre, checked_in)
    add_book(new_book)
    return render_template('books.html', books=books)

@app.route('/books/delete/<title>', methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect('/books')

@app.route('/books/<checked_in>', methods=['POST'])
def update(checked_in):
    update_stock(checked_in)
    return redirect('/books')

    

