import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    virus[start] = 1
    queue = deque(networks[start]) # 큐로 만들기

    while queue:
        now_node = queue.popleft() # 지금 보는 곳 뽑아서 봤다고 확인
        virus[now_node] = 1
        for next_node in networks[now_node]:
            if virus[next_node] == 0: 
                queue.append(next_node) # 안본 곳 큐에 입력


cpus = int(input())
connections = int(input())

networks = [[] for _ in range(cpus+1)]
virus = [0] * (cpus+1)

for _ in range(connections):
    a, b = map(int, input().split())
    networks[a].append(b)
    networks[b].append(a)

bfs(1)
print(sum(virus)-1)