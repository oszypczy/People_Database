from database import Database
from person import Person
from datetime import datetime


def test_database():
    people = [
        Person("1", "Jan Kowalski", "2000-03-01"),
        Person("2", "Jan Kowalski", "2000-03-01"),
    ]
    database = Database(people)

    assert len(database.people) == 2
    assert database.get_person_by_id("1") is people[0]
    assert database.get_person_by_id("2") is people[1]
    assert all(person in database.people.values() for person in people)


def test_database_add_person():
    people = [
        Person("1", "Jan Kowalski", "2000-03-01"),
        Person("2", "Jan Kowalski", "2000-03-01"),
    ]
    database = Database(people)

    person = Person("3", "Jan Kowalski", "2000-03-01")

    database.add_person(person)

    assert len(database.people) == 3
    assert database.get_person_by_id("3") is person
    assert person in database.people.values()


def test_database_create_family_tree():
    grandfather = Person("1", "Jan Kowalski", "1960-06-01")
    grandmother = Person("2", "Anna Wiśniewska", "1962-01-06")
    father = Person('3','Adam Kowalski','1984-03-03', grandfather, grandmother)
    mother = Person('4','Janina Nowak','1980-12-24')
    son = Person('5', 'Stefan Kowalski', '2004-07-28', father, mother)
    people = [grandfather, grandmother, father, mother, son]
    database = Database(people)
    family_tree = database.create_family_tree('5')
    assert len(family_tree) == 5
