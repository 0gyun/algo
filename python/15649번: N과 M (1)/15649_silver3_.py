# from itertools import permutations
# import sys

# input = sys.stdin.readline

# N, M = map(int, input().split())
# N = [idx + 1 for idx in range(N)]
# perms = permutations(N, M)
# for perm in perms:
#     ans = ''
#     for alpha in perm:
#         ans += str(alpha) + ' '
#     print(ans)

import sys

input = sys.stdin.readline

def dfs(made, N, M, cnt):
    for i in range(N):
        if str(i+1) in made:
            continue
        new_made = made + str(i+1) + ' '
        if cnt == M:
            print(new_made)
        else:
            dfs(new_made, N, M, cnt+1)

N, M = map(int, input().split())
dfs('', N, M, 1)
