class personal:
    def __init__(self, name, gender, salary):
        self.name = name
        self.gender = gender
        self.salary = salary


class acadmics:
    def __init__(self, education, marks):
        self.education = education
        self.marks = marks
        self.grade()

    def grade(self):
        if self.marks == 100:
            self.gross = "A"
        elif self.marks >= 75:
            self.gross = "B"
        elif self.marks >= 50:
            self.gross = "C"
        else:
            self.gross = "F"


class skills:
    def __init__(self, skillset):
        self.skillset = skillset


class employe(personal, acadmics, skills):
    def __init__(self, name, gender, salary, education, marks,
                 skillset, empid, depart, company):

        personal.__init__(self, name, gender, salary)
        acadmics.__init__(self, education, marks)
        skills.__init__(self, skillset)

        self.empid = empid
        self.depart = depart
        self.company = company
        self.gross_salary = self.salary * 12

    def display(self):
        print("EMPLOYEE DETAILS")
        print("----------------")
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Monthly Salary:", self.salary)
        print("Annual Gross Salary:", self.gross_salary)
        print("Education:", self.education)
        print("Marks:", self.marks)
        print("Grade:", self.gross)
        print("Skills:", ", ".join(self.skillset))
        print("Employee ID:", self.empid)
        print("Department:", self.depart)
        print("Company:", self.company)


e1 = employe(
    "sawez",
    "male",
    10000,
    "BCS",
    100,
    ["PYTHON", "C", "C++"],
    10,
    "manager",
    "ABClimited"
)

e1.display()