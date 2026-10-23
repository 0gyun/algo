#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25418                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25418                          #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:40:22 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline
start,end = map(int, input().split())
visited = [False for _ in range(1000001)]

queue = deque()
queue.append((start,0))

while True:
    num = queue.popleft()
    if num[0] > end or visited[num[0]]:
        continue
    if num[0] == end:
        print(num[1])
        break
    
    visited[num[0]] = True
    multiple = (num[0] * 2, num[1] + 1)
    plus = (num[0] + 1, num[1] + 1)
    
    queue.append(multiple)
    queue.append(plus)