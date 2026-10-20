v = input("Enter word : ").lower()
count=0

for letter in v:
    if letter in "aeiou":
    
        count +=1
    
print(f"int word {v} total no. of vowels are {count}")
