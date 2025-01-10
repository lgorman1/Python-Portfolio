#Simple Caculator

#Init
#Function
#Adds num1 and num2 and prints the result
def add(num1,num2):
    result = num1 + num2
    print(result)

def sub(num1,num2):
    result = num1 - num2
    print(result)

def multi(num1,num2):
    result = num1 * num2
    print(result)

def div(num1,num2):
    result = num1 / num2
    print(result)

#Main
print("Welcome Preschoolers to Simple Caculator")
while True:
    print("Enter an operation:")
    print("""1. Addition
2. Subtraction
3. Division
4. Multplication
5. Quit""")
    operation = int(input("(1-5)Operation:"))

    if operation == 1: #True
        int1 = int(input("Enter your first number:"))
        int2 = int(input("Enter your second number:"))
        add(int1,int2)

    if operation == 2:
        int1 = int(input("Enter your first number:"))
        int2 = int(input("Enter your second number:"))
        sub(int1,int2)


    if operation == 3:
        int1 = int(input("Enter your first number:"))
        int2 = int(input("Enter your second number:"))
        multi(int1,int2)

    if operation == 4:
        int1 = int(input("Enter your first number:"))
        int2 = int(input("Enter your second number:"))
        div(int1,int2)

    if operation == 5:
        break
       
