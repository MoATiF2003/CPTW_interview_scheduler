from models.book import Book

class Room(Book):
    def __init__(self, room_number):
        super().__init__()
        self.room_number = room_number

    