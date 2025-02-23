from models.book import Book

class Person(Book):
    def __init__(self, name):
        super().__init__()
        self.name = name

