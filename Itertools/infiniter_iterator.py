from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3, 4]

# for x in cycle(a):       #don't use it
#     print(x)

for i in repeat(1, 5):

    print(i)