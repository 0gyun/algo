#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1476                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1476                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:33:44 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

a = 1; b = 1; c = 1
year = 1
while True:
    if E == a and S == b and M == c:
        print(year)
        break
    a += 1
    b += 1
    c += 1
    year += 1
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1
