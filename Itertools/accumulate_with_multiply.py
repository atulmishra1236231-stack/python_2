from itertools import accumulate
import operator
a = [1, 2, 3, 4, 5, 6]
acc = accumulate(a, func=operator.mul)
print(list(acc))