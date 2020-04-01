numberA = int(input("Please enter first number: "))
numberB = int(input("Please enter second number: "))
operation = input("Please choose one of the arithmetic operations (+,-,*,/): ")

if operation == "+":
    print (brojA + brojB)
elif operation == "-":
    print(brojA - brojB)
elif operation == "*":
    print (brojA * brojB)
elif operation == "/":
    print (brojA / brojB)
else:
    print("Invalid operation. Please restart the process.")