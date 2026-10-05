class emplye:
    def __init__(self, employe_id, emp_name, emp_department, emp_designation, emp_city, emp_salary):
        self.employe_id = employe_id
        self.emp_name = emp_name
        self.emp_department = emp_department
        self.emp_designation = emp_designation
        self.emp_city = emp_city
        self.emp_salary = emp_salary
        print("Employees details!")

    def empl_data(self):
        print("employe id:", self.employe_id)
        print("emp_name:", self.emp_name)
        print("emp_department:", self.emp_department)
        print("emp_designation:", self.emp_designation)
        print("emp_city:", self.emp_city)
        print("emp_salary:", self.emp_salary)
        print("annual salary:", self.emp_salary * 12)


e1 = emplye(100, "mrBeast", "saler", "sale manager", "mumbai", 10000)
e1.empl_data()
