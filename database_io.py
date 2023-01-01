from person import Person
from database import Database
import yaml

import csv


class MalformedCSVError(Exception):
    pass


class CSVDataError(Exception):
    pass


def read_database_from_file(handle):
    database = Database([])
    reader = csv.DictReader(handle)
    for row in reader:
        try:
            id = row['id']
            name = row['name']
            birth_date = row['birth_date']
            father_id = row.get('father_id')
            mother_id = row.get('mother_id')
        except KeyError:
            raise MalformedCSVError('CSV headline is invalid')
        father = None
        mother = None
        try:
            if father_id:
                father = database.get_person_by_id(father_id)
            if mother_id:
                mother = database.get_person_by_id(mother_id)
        except KeyError:
            raise CSVDataError('Parent with given id does not exist')
        person = Person(id, name, birth_date, father, mother)
        database.add_person(person)
    return database


def write_database_to_file(handle, database):
    writer = csv.DictWriter(handle, ['id', 'name', 'birth_date', 'father_id', 'mother_id'])
    writer.writeheader()
    for person in database.people.values():
        id = person.id
        name = person.name
        birth_date = person.birth_date
        if person.father:
            father_id = person.father.id
        else:
            father_id = ''
        if person.mother:
            mother_id = person.mother.id
        else:
            mother_id = ''
        writer.writerow({
            'id': id,
            'name': name,
            'birth_date': birth_date,
            'father_id': father_id,
            'mother_id': mother_id
        })


def write_familytree_to_yaml(handle, family_tree):
    yaml.dump(family_tree, handle)