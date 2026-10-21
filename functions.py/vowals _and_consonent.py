
def count_letters(text):
    vowels = 0
    consonants = 0

    for letter in text.lower():
        if letter in "aeiou":
            vowels += 1
        elif letter.isalpha():
            consonants += 1

    return vowels, consonants


sentence = input("Enter any sentence: ")

v, c = count_letters(sentence)

print("Total vowels:", v)
print("Total consonants:", c)
