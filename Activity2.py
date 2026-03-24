class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("The person's name is: ", self.name)
        print("The person's ID number is: ", self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)

a = Employee("Rahul", 886012, 200000, "Intern")
a.display()