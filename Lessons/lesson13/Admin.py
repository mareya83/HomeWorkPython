
from Person.Person import Person

class Admin(Person):
    def __init__(self, name, skill):
        super().__init__(name)
        self.skill = skill

    def hello(self):
        print(f"Hello from admin {self.name}")

    def best_skill(self):
        print(f"He {self.skill} the best")