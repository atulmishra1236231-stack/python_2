try:
    enter = input("Enter Eile Name : ")
    with open(enter, "r") as file:
        content = file.read()
        print(content)
except:
    print("File not found")