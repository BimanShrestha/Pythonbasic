def greet(name):
    
    print("Hello, " + name + ". Good morning!")

greet('Biman')

def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

# Program to illustrate
# the use of user-defined functions

def add_numbers(x,y):
   sum = x + y
   return sum

num1 = 5
num2 = 6

print("The sum is", add_numbers(num1, num2))

def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Biman", "Good morning!")