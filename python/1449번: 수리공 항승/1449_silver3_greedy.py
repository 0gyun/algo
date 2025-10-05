import sys

input = sys.stdin.readline

n, l = map(int, input().split())

places = list(map(int, input().split()))
places.sort()

now = places[0]
cnt = 1
for hole in places[1:]:
    if hole - now + 1 <= l:
        continue
    else:
        now = hole
        cnt += 1
        
print(cnt)