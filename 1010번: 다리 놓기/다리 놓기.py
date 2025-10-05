#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1010                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1010                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:25:58 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import math

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N, M = map(int,input().split())
    comb = math.comb(M,N)
    print(comb)