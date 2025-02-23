from models.book import Book

def test_is_free():
    book = Book()
    assert book.is_free(9) == True

def test_book_interview():
    book = Book()
    book.book_interview(9)
    assert book.is_free(9) == False
    assert book.is_free(11) == True
