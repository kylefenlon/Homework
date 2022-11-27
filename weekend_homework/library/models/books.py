from models.book import Book

book1 = Book("The subtle art of not giving a f***", "Mark Ronson", "Non-fiction", True)
book2 = Book("Game of Thrones", "George R.R. Martin", "Fiction", False)
book3 = Book("The Chimp Paradox", "Steve Peters", "Non-fiction", True)

books = [book1, book2, book3]

def book_has_title(book):
    return book["title"]

def book_has_author(book):
    return book["author"]

def get_book(book_index):
    return books[book_index]

def add_book(book):
    books.append(book)

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break
    books.remove(book_to_delete)

def update_stock(book_checked_in):
    book_checked_in = None
    for book in books:
        if book.checked_in == True:
            book_checked_in = book
        books.append(book_checked_in)

    
