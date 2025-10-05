import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.insert(0, int(input()))

ans = 0
for coin in coins:
    if K // coin >= 0:
        ans += K // coin
        K = K % coin

print(ans)