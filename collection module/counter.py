from collections import Counter
a = "aaabbbcccccfsaaa"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common(1))