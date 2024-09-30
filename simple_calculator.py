operator = input("Enter an operator(+ - * /): ")
num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is : {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is : {result}")
elif operator == "+":
    result = num1 * num2
    print(f"The product of {num1} and {num2} is : {result}")
elif operator == "/":
    result = num1 / num2
    print(f"The quotient of {num1} and {num2} is : {result}")
else:
    print(f"{operator} is not a valid operator")