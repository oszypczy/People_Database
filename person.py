from datetime import date

class Person:
    def __init__(self, id, name, birth_date, father=None, mother=None, children=None) -> None:
        self.id = id
        self.name = name
        self.birth_date = date.fromisoformat(birth_date)
        self.father = father
        self.mother = mother
        if not children:
            self.children = []
        else:
            self.children = children
        if mother:
            mother.children.append(self)
        if father:
            father.children.append(self)

    def set_father(self, new_father):
        new_father.children.append(self)
        self.father = new_father

    def set_mother(self, new_mother):
        new_mother.children.append(self)
        self.mother = new_mother

    def oldest_sibling(self):
        if not self.mother and not self.father:
            return None
        if self.mother:
            siblings_after_mother = self.mother.children
        if self.father:
            siblings_after_father = self.father.children
        all_siblings = list(set(siblings_after_mother + siblings_after_father))
        if len(all_siblings) < 2:
            return None
        sorted_siblings = sorted(all_siblings, key=lambda sibling: sibling.birth_date)
        return sorted_siblings[0]
