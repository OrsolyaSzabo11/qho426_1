

class Database:

    def __init__(self):
      self.name = "Piotr's Database"
      self.people = []
      self.num_of_people = len(self.people)

    def add_person(self, p):
        self.people.append(p)

    def remove_person(self, p):
        self.people.remove(p)

    def display_all(self):
        for person in self.people:
            person.hello()

p1 = Person("Orsi", 27)
p2 = Person("Wesley")
p3 = Person("Stefan", jon = "Programmer", energy = 87)
db = Database()
print(f"{db.name} contains {db.num_of_people} objects")
db.add_person(p2)
db.add_person(p3)
db.add_person(p1)
db.display_all()
print(f"{db.name} contains {db.num_of_people} objects")