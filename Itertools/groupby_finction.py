from itertools import groupby
def less_then_3(x):
    return x<3

a = [1, 2, 3, 4]
x = groupby(a, key = less_then_3) # return true or false

# print (list(group_obj))
# print(bool(group_obj), "\n")

for i, value in x:
    print(i, list(value))

print(x)