#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2018                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2018                           #+#        #+#      #+#     #
#    Solved: 2025/10/09 21:50:48 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())

start, end, total = 1, 1, 1
cnt = 0

while start <= N:
    if total == N:
        cnt += 1
        total -= start
        start += 1
    elif total > N:
        total -= start
        start += 1
    else:
        end += 1
        total += end
print(cnt)