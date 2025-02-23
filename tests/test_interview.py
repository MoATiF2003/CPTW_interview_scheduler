from models.person import Person
from models.room import Room
from models.interview import Interview

def test_interview_booking():
    attendee = Person("Alice")
    interviewer = Person("Bob")
    room = Room(101)
    
    interview = Interview(attendee, interviewer, room, 9)
    assert interview.book_interview() == True
