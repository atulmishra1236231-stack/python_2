def factorial(n):
    m = 1
    for i in range(n):
        if n!=0:
            m = m*n
            n = n-1
    return m

    

n = int(input("Enter any non -ve no. I will find falctorial of it : "))

print(factorial(n))