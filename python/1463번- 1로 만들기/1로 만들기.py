#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1463                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1463                           #+#        #+#      #+#     #
#    Solved: 2025/10/09 17:56:07 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

input = sys.stdin.readline

N = int(input())

cnts = [0 for _ in range(N+1)]

for i in range(2, N+1):
    a = cnts[i-1] + 1
    if i % 2 == 0:
        b = cnts[i//2] + 1
        a = min(a, b)
    if i % 3 == 0:
        b = cnts[i // 3] + 1
        a = min(a,b)
    cnts[i] = a
    
print(cnts[N])