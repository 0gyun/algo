#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1449                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1449                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:33:26 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

n, l = map(int, input().split())

places = list(map(int, input().split()))
places.sort()

now = places[0]
cnt = 1
for hole in places[1:]:
    if hole - now + 1 <= l:
        continue
    else:
        now = hole
        cnt += 1
        
print(cnt)