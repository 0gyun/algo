#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2839                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2839                           #+#        #+#      #+#     #
#    Solved: 2025/10/05 12:15:48 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())

ans = 5001
loops = N // 5
cnt = 0
for _ in range(loops+1):
    if not N % 3:
        tmp = N // 3
        ans = cnt + tmp if ans > cnt + tmp else ans
    N -= 5
    cnt += 1
if ans == 5001:
    print(-1)
else:
    print(ans)