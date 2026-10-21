def Convert_Fahrenheit(c):
    F = (c * 9/5) + 32
    return F

celsius = float(input("Enter temperature in calsius! I will convert it in faharenhit : "))

print(Convert_Fahrenheit(celsius))