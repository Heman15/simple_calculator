def add (a,b):
    return a+b
def multiply (a,b):
    return a*b
def subtract(a,b):
    return a - b
def division(a,b):
    return a/b
print("1. Addition")
print("2. multiply")
print("3. subtract")
print("4. subtract")
choice = int(input("Enter your choice 1,2,3,4"))
num1 = float(input("enter the number"))
num2 = float(input("enter the number"))
if choice == 1:
    print("Addition of {0} and {1} is {2}".format(num1, num2, add(num1,num2)))
elif choice == 2:
    print("Multiplication of {0} and {1} is {2}".format(num1, num2, multiply(num1,num2)))
elif choice == 3:
    print("Subtraction of {0} and {1} is {2}".format(num1, num2, subtract(num1,num2)))
elif choice == 4:
    print("Division of {0} and {1} is {2}".format(num1, num2, division(num1,num2)))
else:
    print("invalid choice")