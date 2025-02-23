from models.room import Room

def test_room_is_free():
    room = Room(101)
    assert room.is_free(9) == True

def test_room_booking():
    room = Room(101)
    room.book_interview(9)
    assert room.is_free(9) == False
