from models.person import Person

def test_person_is_free():
    person = Person("Alice")
    assert person.is_free(9) == True

def test_person_booking():
    person = Person("Alice")
    person.book_interview(9)
    assert person.is_free(9) == False
    assert person.is_free(11) == True
