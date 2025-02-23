from models.person import Person
from models.room import Room

class Interview:
    def __init__(self, attendee, interviewer, room, start_time):
        self.attendee = attendee
        self.interviewer = interviewer
        self.room = room
        self.start_time = start_time
        self.end_time = start_time + 2

    def book_interview(self):
        if self.attendee.is_free(self.start_time)  and  self.interviewer.is_free(self.start_time)  and  self.room.is_free(self.start_time):
            self.attendee.book_interview(self.start_time)
            self.interviewer.book_interview(self.start_time)
            self.room.book_interview(self.start_time)
            return True
        return False
    
    def __str__(self):
        return f"{self.attendee.name} is sheduled with {self.interviewer.name} in Room{self.room.room_number} from {self.start_time}:00 to {self.end_time}:00"