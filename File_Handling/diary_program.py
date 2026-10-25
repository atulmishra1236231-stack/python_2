entry = input("write form here : ")
with open("diary.txt", "a") as file:
    content = file.write(entry + "\n")
print("Diary entry saved successfully!")