import sys
input = sys.stdin.readline

num_trees = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
left_days = 0
total_days = 0
for tree in trees:
    left_days = max(left_days, tree + 1)
    left_days -= 1
    total_days += 1

total_days += left_days + 1
print(total_days)