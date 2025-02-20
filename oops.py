#basic example
class first:
    x = 50
obj = first()
print(obj.x)
#classes and objects
class faculty:
    def putdata(self):
        self.id=int(input("enter facultyid:"))
        self.name=input("enter name:")
        self.salary = float(input("enter faculty salary:"))
    def display(self):
        print("faculty id:" ,self.id)
        print("faculty name:" ,self.name)
        print("faculty salary:" ,self.salary)
a = faculty()
a.putdata()
a.display()

#constructors
class faculty:
    def __init__(self):
        self.id=int(input("enter facultyid:"))
        self.name=input("enter name:")
        self.salary = float(input("enter faculty salary:"))
    def display(self):
        print("faculty id:" ,self.id)
        print("faculty name:" ,self.name)
        print("faculty salary:" ,self.salary)
a = faculty()
a.display()
#parameter passing 
class faculty:
    def __init__(self,a,b,c):
        self.id=a
        self.name=b
        self.salary = c
    def display(self):
        print("faculty id:" ,self.id)
        print("faculty name:" ,self.name)
        print("faculty salary:" ,self.salary)
a = faculty(1,"varun",10000)

a.display()


