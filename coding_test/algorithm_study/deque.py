from collections import deque

dq = deque()
dq = deque('1234')
dq.append("5")
dq.appendleft("0")
removed = dq.pop()
print(removed)
removed = dq.popleft()
print(removed)
dq.rotate(1)

while len(dq):
    print(dq[0])
    dq.popleft()