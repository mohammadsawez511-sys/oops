class student:

    school_name = "ATT hing school"

    @classmethod
    def display_info(cls,year):
        print("ATT hing school build date ")
        cls.year = year
        print(year)
    
    
    def __init__(self,name,roll_no,marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks
        

    def display_details(self):
        print("student details ")
            
        print("----------------")
        print("name =",self.name )
        print("roll number = ",self.roll_no)
        print("marks = ",self.marks)


e1 =student("sawez",22,100)
e1.display_details()
student.display_info(1999)
        