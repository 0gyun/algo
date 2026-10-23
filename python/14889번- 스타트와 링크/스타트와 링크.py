#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14889                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14889                          #+#        #+#      #+#     #
#    Solved: 2025/10/09 19:00:17 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
stats = []

for _ in range(N):
    r = list(map(int, input().split()))
    stats.append(r)

min_diff = -1

comb = list(combinations(range(N), N//2))
for idx in range(len(comb)//2):
    teamA = comb[idx]
    teamB = comb[len(comb) - (idx+1)]
    teamA_stat = 0
    teamB_stat = 0
    for i in range(len(teamA)):
        for j in range(len(teamA)):
            if i == j:
                continue
            teamA_stat += stats[teamA[i]][teamA[j]]
            teamB_stat += stats[teamB[i]][teamB[j]]
    diff = teamA_stat - teamB_stat if teamA_stat > teamB_stat else teamB_stat - teamA_stat
    if min_diff == -1 or min_diff > diff:
        min_diff = diff
        
print(min_diff)