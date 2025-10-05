#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2667                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2667                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:36:33 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
town = []
houses = []
visited = [[False for _ in range(N)] for _ in range(N)]
for idx in range(N):
    row = list(input())
    # 리스트에서 특정 원소의 인덱스를 모두 뽑는 filter 함수
    all_index = list(filter(lambda x: row[x] == '1', range(len(row))))
    town.append(row)
    if all_index:
        houses.append(all_index)
    else:
        houses.append(0)

queue = deque()
num_houses = []
for row in range(len(houses)):
    if houses[row] == [0]:
        continue
    for house in houses[row]:
        if visited[row][house]:
            continue
        start = (row, house)
        queue.append(start)
        cnt = 0
        while queue:
            now = queue.popleft()
            y = now[0]
            x = now[1]
            if visited[y][x] or town[y][x] == '0':
                continue
            
            visited[y][x] = True
            cnt += 1
            if x:
                next = (y, x-1)
                queue.append(next)
            if x < N-1:
                next = (y, x+1)
                queue.append(next)
            if y:
                next = (y-1, x)
                queue.append(next)
            if y < N-1:
                next = (y+1, x)
                queue.append(next)
        if cnt:
            num_houses.append(cnt)
        
num_houses.sort()
print(len(num_houses))
for num in num_houses:
    print(num)