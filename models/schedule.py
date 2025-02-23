import json
from models.person import Person
from models.room import Room
from models.interview import Interview

class Schedule:
    def __init__(self, attendees, interviewers, rooms): #attendees and interviewers are the list of names and rooms denotes the numnber of rooms available
        self.attendees = attendees
        self.interviewers = interviewers
        self.rooms = rooms

    def schedule_interview(self): #attendees and interviewers are the list of names and rooms denotes the numnber of rooms available
        # Fixed time slots as numbers: 9 (9-11), 11 (11-1), 15 (3-5)
        time_slots = [9, 11, 15]

        #creating Objects 
        attendee_list = [Person(name) for name in self.attendees] # list of objects of Person
        interviewer_list = [Person(name) for name in self.interviewers] # list of objects of Person
        room_list = [Room(i + 1) for i in range(self.rooms)] # list of objects of Room

        scheduled = [] # list of confirmed or scheduled interview object
        unscheduled = [] # list of unconfirmed or unscheduled attendee name

        # Simple scheduling: try each attendee with first available slot
        for attendee in attendee_list:
            booked = False
            for start_time in time_slots:
                for interviewer in interviewer_list:
                    for room in room_list:
                        interview = Interview(attendee, interviewer, room, start_time)
                        if interview.book_interview():
                            scheduled.append({
                                "attendee" : interview.attendee.name,
                                "interviewer" : interview.interviewer.name,
                                "room" : interview.room.room_number,
                                "start_time" : interview.start_time,
                                "end_time" : interview.end_time
                            })
                            booked = True
                            break
                    if booked:
                        break
                if booked:
                    break
            if not booked:
                unscheduled.append(attendee.name)

        self.save_to_json(scheduled, unscheduled)

        print("Scheduled Interviews:")
        for interview in scheduled:
            print(f"{interview['attendee']} is scheduled with {interview['interviewer']} in Room {interview['room']} from {interview['start_time']} to {interview['end_time']}")

        print()
        if unscheduled:
            print("Could not schedule for:")
            for attendee in unscheduled:
                print("-", attendee)

    def save_to_json(self, scheduled, unscheduled):
        data = {
            "scheduled" : scheduled,
            "unscheduled" : unscheduled
        }
        with open("schedule.json", "w") as f:
            json.dump(data, f, indent=4)
        

        
       
