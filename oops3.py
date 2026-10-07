
# this is parents class or super clss 
class parents:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        print("parents class")

    def display_info(self):
        print(self.name)
        print(self.age)
        

# this is child class or subclass 
class child(parents):
    def __init__(self, name, age,id,roll_number):
        super().__init__(name,age,)
        self.id = id 
        self.roll_number = roll_number
        print("child class ")

    def display(self):
        print(self.id)
        print(self.roll_number)
       


s1 = child("sawez",18,1010,22)
s1.display_info()
s1.display()        

  

class user:
    def __init__(self,username,password):
        self.username = username 
        self.password = password

    def show_user(self):
        print("username :",self.username)    


class admin(user):
    def check_password(self,password):
        if self.password == password:
            print("correct password ")
        else:
            print("wrong password ")    

a = admin("sawez",1000)
a.show_user()
a.check_password(1000)


        
   