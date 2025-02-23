class Book:
    def __init__(self):
        self.schedule = [] # List of (start_time, end_time) as numbers

    def is_free(self, start_time):
        for booked_startTime, booked_endTime in self.schedule:
            if start_time >= booked_startTime and start_time < booked_endTime:
                return False
        return True

    def book_interview(self, start_time):
        end_time = start_time + 2  # Each interview is 2 hours
        self.schedule.append((start_time, end_time))
    