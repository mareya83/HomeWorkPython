# 1) Create app.py
# 2) Create package Person -> Into Person create file Person.py -> 
# 2.1) Create file Admin.py
# 2) Admin extends Person
# 3) Create instance Admin into app.py 
# 3.1) Into app.py create function or class(method) that will run our program . 
# 4) If app.py == __main__ => run program 
import random
from Admin import Admin

skills = ["works", "promises to do everything", "says he's busy", "tells stories"]
names = ["Bob", "Nik", "Jak"]

class Run:
    
    @staticmethod
    def Start():
        admin = Admin(random.choice(names), random.choice(skills))
        admin.hello()
        admin.best_skill()



if __name__ == "__main__":

   Run.Start()


