class Employee:
    def __init__(self, fname, lname, salary):
        self.fname =fname
        self.lname =lname
        self.salary =salary

ram = Employee('ram','bahadur', 44000)
sam = Employee('sam','bahadur', 44000)

print(ram.fname, sam.fname)
