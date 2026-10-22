from math import factorial

num = int(input("Enter number : "))
if num<0:
    print("please enter positive integer")
else:
    print(f"Factorial of {num} is {factorial(num)}")