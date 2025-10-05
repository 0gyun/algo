import sys

input = sys.stdin.readline
num_candidates = int(input())
votes_per_candidates = []
mine = int(input())
for _ in range(num_candidates-1):
    votes = int(input())
    if votes >= mine:
        votes_per_candidates.append(votes)

if len(votes_per_candidates)==0:
    print(0)
else:
    init_mine = mine
    lefts = sorted(votes_per_candidates, reverse=True)
    cnt = 0
    while mine <= max(lefts):
        m = max(lefts)
        mine += 1
        cnt += 1
        lefts[0] -= 1
        lefts.sort(reverse=True)

    print(cnt)
