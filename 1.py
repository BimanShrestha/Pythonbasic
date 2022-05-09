#This is a python progrm to find greatest number between 3 numberss
a=input("enter 1 number: \n")
b=input("enter 2 number: \n") 
c=input("enter 3 number: \n") 
num1=int(a)
num2=int(b)
num3=int(c) 

if(num1>num2 and num1>num3):
    print("Number 1 is great")
elif(num2>num1 and num2>num3):
    print("Number 2 is great")
elif(num3>num1 and num3>num2):
    print("Number 3 is great")
else:
    print("other than number 1 is great")




