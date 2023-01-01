class Database:
    def __init__(self, people):
        self.people = {}
        for each_person in people:
            self.people[each_person.id] = each_person

    def get_person_by_id(self, id):
        return self.people[id]

    def add_person(self, new_person):
        self.people[new_person.id] = new_person

    def create_family_tree(self, id):
        family_tree = {}
        family_tree['id'] = id
        family_tree['name'] = self.people[id].name
        family_tree['birth_date'] = self.people[id].birth_date
        if self.people[id].father:
            family_tree['father'] = self.create_family_tree(self.people[id].father.id)
        if self.people[id].mother:
            family_tree['mother'] = self.create_family_tree(self.people[id].mother.id)
        return family_tree