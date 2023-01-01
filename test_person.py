from person import Person
from datetime import date


def test_person_create_without_family():
    person = Person("1", "Jan Kowalski", "2000-03-01")

    assert person.id == "1"
    assert person.name == "Jan Kowalski"
    assert person.birth_date == date.fromisoformat("2000-03-01")
    assert person.mother is None
    assert person.father is None
    assert len(person.children) == 0


def test_person_create_with_family():
    mother = Person("2", "Janina Kowalska", "1980-03-01")
    father = Person("3", "Adam Kowalski", "1978-03-01")

    person = Person("1", "Jan Kowalski", "2000-03-01", father, mother)

    assert person.id == "1"
    assert person.name == "Jan Kowalski"
    assert person.birth_date == date.fromisoformat("2000-03-01")
    assert person.mother is mother
    assert person.father is father
    assert len(person.children) == 0
    assert person in mother.children
    assert person in father.children


def test_person_set_father():
    father = Person("3", "Adam Kowalski", "1978-03-01")
    person = Person("1", "Jan Kowalski", "2000-03-01")

    person.set_father(father)

    assert person.father is father
    assert person in father.children


def test_person_set_mother():
    mother = Person("2", "Janina Kowalska", "1980-03-01")
    person = Person("1", "Jan Kowalski", "2000-03-01")

    person.set_mother(mother)

    assert person.mother is mother
    assert person in mother.children


def test_person_get_oldest_sibling_no_parents_set():
    assert Person("1", "Jan Kowalski", "2000-03-01").oldest_sibling() is None


def test_person_get_oldest_sibling_only_child():
    mother = Person("2", "Janina Kowalska", "1980-03-01")
    father = Person("3", "Adam Kowalski", "1978-03-01")
    person = Person("1", "Jan Kowalski", "2000-03-01", father, mother)

    assert person.oldest_sibling() is None


def test_person_get_oldest_sibling():
    mother = Person("2", "Janina Kowalska", "1980-03-01")
    father = Person("3", "Adam Kowalski", "1978-03-01")
    siblings = [
        Person("4", "Jan Kowalski", "1999-10-20", mother=mother, father=father),
        Person("5", "Jan Kowalski", "1998-09-22", mother=mother),
        Person("6", "Jan Kowalski", "2001-03-02", father=father),
    ]
    person = Person("1", "Jan Kowalski", "2000-03-01", mother=mother, father=father)
    assert person.oldest_sibling() is siblings[1]
