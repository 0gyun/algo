#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18429                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18429                          #+#        #+#      #+#     #
#    Solved: 2025/10/09 18:07:19 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
inc = list(map(int, input().split()))

ans = 0
used = [False for _ in range(N)]

def dfs(i, lift):
    lift += inc[i] - K
    if lift < 500:
        return 0
    if sum(used) == N:
        return 1
    cnt = 0
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        cnt += dfs(i, lift)
        used[i] = False
    return cnt
    
for i in range(N):
    used[i] = True
    ans += dfs(i, 500)
    used[i] = False
print(ans)