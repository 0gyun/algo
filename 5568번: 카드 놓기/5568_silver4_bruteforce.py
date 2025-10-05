import sys
from itertools import permutations # 순열을 사용

input = sys.stdin.readline

N = int(input())
K = int(input())
cards = []
for _ in range(N):
    cards.append(input().strip())

perms = list(permutations(cards, K)) # permutations(리스트, 뽑을 개수)
new_num = []
for nums in perms:
    num = int(''.join(nums)) # 튜플의 원소들을 하나의 문자열로 합치는 방법
    if num not in new_num:
        new_num.append(num)
print(len(new_num))