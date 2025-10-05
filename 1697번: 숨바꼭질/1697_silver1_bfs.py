import sys
from collections import deque

input = sys.stdin.readline

subin, bro = map(int, input().split())

visited = [False for _ in range(100001)]

queue = deque()
queue.append((subin,0))

while True:
    num = queue.popleft()
    if num[0] < 0 or num[0] > 100000 or visited[num[0]]:
        continue
    if num[0] == bro:
        print(num[1])
        break
    
    visited[num[0]] = True
    multiple = (num[0] * 2, num[1] + 1)
    plus = (num[0] + 1, num[1] + 1)
    minus = (num[0] -1, num[1] + 1)
    
    queue.append(multiple)
    queue.append(plus)
    queue.append(minus)