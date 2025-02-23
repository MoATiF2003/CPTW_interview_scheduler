from models.schedule import Schedule

if __name__ == "__main__":
    attendees = ["Martin", "Jimmy", "John", "Sandra", "Bobby", "Denis", "Garnacho"]
    interviewers = ["interviewer1", "interviewer2"]
    rooms = 2

    schedule = Schedule(attendees, interviewers, rooms)

    schedule.schedule_interview()