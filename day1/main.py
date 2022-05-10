class Employee:
    increment =1.5
    no_of_employee=0
    def __init__(self, fname, lname, salary):
        self.fname =fname
        self.lname =lname
        self.salary =salary
        Employee.no_of_employee +=1
    def increase(self):
        self.salary=self.salary *Employee.increment
print(Employee.no_of_employee)
ram = Employee('ram','bahadur', 44000)
sam = Employee('sam','bahadur', 44000)
print(Employee.no_of_employee)
#print(ram.fname, sam.fname)
#print(Employee.__dict__)
#print(ram.__dict__)
#print(sam.__dict__)
