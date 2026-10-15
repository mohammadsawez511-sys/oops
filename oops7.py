class person:
    def __init__(self, name, city):
        self.name = name
        self.city = city


class acadmics(person):
    def __init__(self, name, city, grade, education):
        person.__init__(self, name, city)
        self.grade = grade
        self.education = education


class skill(person):
    def __init__(self, name, city, skill_set):
        person.__init__(self, name, city)
        self.skill_set = skill_set


class employe(acadmics, skill):
    def __init__(self, name, city, grade, education, skill_set, company):
        acadmics.__init__(self, name, city, grade, education)
        skill.__init__(self, name, city, skill_set)
        self.company = company


emp1 = employe(
    "sawez", "Malegaon", "A", "BCS",
    "Python, sleeping", "ABCD"
)

print(emp1.name)
print(emp1.city)
print(emp1.grade)
print(emp1.education)
print(emp1.skill_set)
print(emp1.company)