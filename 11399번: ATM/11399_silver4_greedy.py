import sys

input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort()

prev = 0
total = 0
for time in times:
    total += time
    prev += total
    
print(prev)