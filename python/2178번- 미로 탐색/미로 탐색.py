#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2178                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2178                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:35:53 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [[False for _ in range(M)] for _ in range(N)]
maze = []
for idx in range(N):
    row = list(input())
    maze.append(row)

queue = deque()
queue.append((0,0,1))
while True:
    now = queue.popleft()
    if now[0] == N-1 and now[1] == M-1:
        print(now[2])
        break
    
    if visited[now[0]][now[1]] or maze[now[0]][now[1]] == '0':
        continue
    
    visited[now[0]][now[1]] = True
    
    if now[1]:
        left= (now[0],now[1]-1,now[2]+1)
        queue.append(left)
    if now[1]+1 < M:
        right = (now[0],now[1]+1,now[2]+1)
        queue.append(right)
    if now[0]:
        up = (now[0]-1,now[1],now[2]+1)
        queue.append(up)
    if now[0]+1 < N:
        down = (now[0]+1,now[1],now[2]+1)
        queue.append(down)

