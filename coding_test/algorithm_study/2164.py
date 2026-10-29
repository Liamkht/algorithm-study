from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque()
for i in range(1, N+1):
    dq.append(i)

while len(dq):
    dq.popleft()
    dq.rotate(1)