def number_vowals(v):
    count = 0

    for letter in v:
        if letter in "aeiou":
            count+=1
        
    return count
   
    

v = input("enter any sentence and I will count no. of vowels in your sentence : ").lower()
r = v.replace(" ", "")
c=number_vowals(r)

print(f"Total_vowals : {c}")
print("total consonents : " ,len(r)-c)

    
    
   

