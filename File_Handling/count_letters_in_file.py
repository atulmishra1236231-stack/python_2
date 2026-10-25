with open("diary.txt", "r") as file:
    content = file.read()
    result = content.split()

    print(len(result))
