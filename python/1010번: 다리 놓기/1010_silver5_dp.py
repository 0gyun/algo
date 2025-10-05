import sys
import math

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N, M = map(int,input().split())
    comb = math.comb(M,N)
    print(comb)