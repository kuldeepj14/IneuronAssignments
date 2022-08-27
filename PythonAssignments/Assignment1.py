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
findMaxNum()