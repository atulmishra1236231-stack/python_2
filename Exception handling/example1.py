try:
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))

    print("1st/2nd : ", num1/num2)
    
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("can not be divided by zero")
else:
    print("division sucessfull")
finally:
    print("calculater close")

    