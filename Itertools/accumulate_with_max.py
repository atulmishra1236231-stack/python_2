from itertools import accumulate
import operator
a = [1, 3, 4, 8, 12,1, 3, 5, 9, 14, 5, 6]
acc = accumulate(a, func=max)
print(list(acc))