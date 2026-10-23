#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2579                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2579                           #+#        #+#      #+#     #
#    Solved: 2025/10/05 21:30:51 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

input = sys.stdin.readline

num_stairs = int(input())
stairs = []
for _ in range(num_stairs):
    stair = int(input())
    stairs.append(stair)

# def score(stair, consequences):
#     if stair < 0:
#         return 0
#     if consequences == 1:
#         return stairs[stair] + score(stair - 2, 0)
#     else:
#         return stairs[stair] + max(score(stair - 1, consequences + 1), score(stair - 2, 0))

# print(score(num_stairs-1, 0))

max_scores = [[0] for _ in range(num_stairs)]

max_scores[0] = stairs[0]
if num_stairs > 1:
    max_scores[1] = stairs[0] + stairs[1]
if num_stairs > 2:
    max_scores[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for idx in range(3, num_stairs):
        a = max_scores[idx - 2] + stairs[idx]
        b = max_scores[idx-3] + stairs[idx-1] + stairs[idx]
        max_scores[idx] = max(a,b)

print(max_scores[num_stairs-1])