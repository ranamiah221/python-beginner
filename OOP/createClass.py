class Student:
    def __init__(self, name, marks=0):
        self.name=name
        self.marks=marks
        print("Adding student info into the database:")
        

s1=Student("Rana", 33)
print(s1.name, s1.marks)

s2=Student("Hasan",100)
print(s2.name, s2.marks)
