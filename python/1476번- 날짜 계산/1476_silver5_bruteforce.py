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
