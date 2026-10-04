from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)