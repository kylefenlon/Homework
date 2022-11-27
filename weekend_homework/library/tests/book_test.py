import unittest
from models.books import add_book, get_book, book_has_author, book_has_title
from models.book import Book

class TestBook(unittest.TestCase):
    
    
    def setUp(self):
        self.book1 = Book("The subtle art of not giving a f***", "Mark Ronson", "Non-fiction", True)
        self.book2 = Book("Game of Thrones", "George R.R. Martin", "Fiction", False)
        self.book3 = Book("The Chimp Paradox", "Steve Peters", "Non-fiction", True)
        self.books = [self.book1, self.book2, self.book3]

    def test_book_has_title(self):
        self.assertEqual("The Chimp Paradox", self.book3.title)
    
    def test_book_has_author(self):
        self.assertEqual("Steve Peters", self.book3.author)

    def test_book_genre(self):
        self.assertEqual("Fiction", self.book2.genre)

    def test_book_in_stock(self):
        self.assertEqual(True, self.book1.checked_in)