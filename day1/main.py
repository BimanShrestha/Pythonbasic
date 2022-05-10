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
    @classmethod
    def change_increment(cls,amount):
     cls.increment =amount
    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary =emp_string.split("-")
        return cls(fname, lname, salary)
    @staticmethod
    def isopen(day):
        if day =="sunday":
            return False
        else:
            return True
print(Employee.isopen('sunday'))            
            


#print(Employee.no_of_employee)
#ram = Employee('ram','bahadur', 44000)
#sam = Employee('sam','bahadur', 44000)
#hari = Employee.from_str("hari-bahadur-76000")
#print(hari.lname)
#print(ram.salary)
#Employee.change_increment(2)
#ram.increase()
#print(ram.salary)
#print(Employee.no_of_employee)
#print(ram.fname, sam.fname)
#print(Employee.__dict__)
#print(ram.__dict__)
#print(sam.__dict__)
