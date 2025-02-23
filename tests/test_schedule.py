from models.schedule import Schedule

def test_schedule():
    attendees = ["Alice", "Bob"]
    interviewers = ["Interviewer1"]
    rooms = 1

    schedule = Schedule(attendees, interviewers, rooms)
    assert schedule.schedule_interview() is None  # Just checking if it runs without error
