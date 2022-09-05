"""

Please comment the functions once checked


"""

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
def divisibleNums():
    divisibleNumList = []
    for i in range(1500,2701):
        if (i%7 == 0) and (i%5 == 0):
            divisibleNumList.append(i)
    print(divisibleNumList)
# divisibleNums()


# 2. Python program to add two numbers
def addNums():
    x = int(input("add first number: "))
    y = int(input("add second number: "))
    addTwoNumbers = x + y 
    print(f"Sum of {x} and {y} is: ", addTwoNumbers)
# addNums()


# 3. Maximum of two numbers in Python
def findMaxNum():
    x = int(input("add first number: "))
    y = int(input("add second number: "))
    if x > y:
        print(f"{x} is greater then {y}.")
    elif x < y:
        print(f"{y} is greater then {x}.")
    else:
        print(f"both numbers are equal.")
# findMaxNum()


# 4. Python Program for factorial of a number
def numFactorial():
    num = int(input("enter the number: "))
    fac = 1
    if num<0:
        print("Factorial does not exist for negative numbers")
    elif num==0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, num+1):
            fac = fac * i
        print(f"Factorial of {num} is {fac}")
# numFactorial()


# 5. Python Program for simple interest
def findSimpleInterest():
    principal = int(input("What is the amount: "))
    interest = float(input("What is the interest: "))
    time = float(input("What is the duration for which the principal amount is given: "))
    simpleInterest = ( principal * interest * time ) / 100
    print(f"Simple interest s: {simpleInterest}")
# findSimpleInterest()


# 6. Python Program for compound interest
def findCompundInterest():
    principal = int(input("What is the amount: "))
    interest = float(input("What is the interest: "))
    time = float(input("What is the duration for which the principal amount is given: "))
    amount = principal * (1 + (interest/100)) ** time
    compoundInterest = amount - principal
    print(f"Compound Interest Value: {compoundInterest}")
# findCompundInterest()


# 7. Python Program to check Armstrong Number

