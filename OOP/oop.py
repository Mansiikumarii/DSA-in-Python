'''
Object- oriented program (OOP) is a paradigm that uses object and classes to design and structure code.
'''

class Student: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
        
    def display(self): 
        print(f"Name: {self.name}, Age: {self.age}") 

# Creating object 
s1 = Student("Anupriya", 24) 
s1.display()

'''
Key Concepts of OOP

- Class and Object
- Class : A blue print for creating objects
- Object : An instance of class
'''

class DA_Students:
    def __init__(self, name, roll_no, branch, year, score):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.year = year
        self.score = score
    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_no} ")
        print(f"Branch : {self.branch}")
        print(f"Year: {self.year}")
        print(f"Score :{self.score}")
        print("_"*30)
Std1 = DA_Students("Priyanshi","DA2030","DS & AI", 2027, 80)
Std2 = DA_Students("Khushi","DA20234","DS&AI", 2027,98.97)
Std1.display_info()
Std2.display_info()