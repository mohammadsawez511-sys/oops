class employe:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name )
        print(self.id )
         

class p(employe):
    def __init__(self, name, id,parfomance):

        super().__init__(name, id)
        self.parfomance = parfomance

    def display_p(self):
            
        super().display()
        print(self.parfomance)

class s(employe):
    def __init__(self, name, id,skills):
        super().__init__(name, id)
        self.skills = skills

    def display_s(self):
        super().display()
        print(self.skills)    

class q(employe):
    def __init__(self, name, id,work):
        super().__init__(name, id)
        self.work = work

    def display_q(self):
        super().display()
        print(self.work)     

s1 = p("noman",101,"HIHG")
s2 = s("abdurheman",102,"PYTHON")
s3 = q("nawaz",103,"NOTHING")
s1.display_p()
s2.display_s()
s3.display_q()
