#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14888                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14888                          #+#        #+#      #+#     #
#    Solved: 2025/10/09 18:34:31 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
add = ['a'] * ops[0]
mi = ['m'] * ops[1]
mul = ['x'] * ops[2]
div = ['d'] * ops[3]
ops = add + mi + mul + div

ans = [None, None] # min, max
perm = permutations(ops)
ops_set = set(perm)

for o in ops_set:
    num = nums[0]
    for idx, op in enumerate(o):
        if op == 'a':
            num += nums[idx+1]
        if op == 'm':
            num -= nums[idx+1]
        if op == 'x':
            num *= nums[idx+1]
        if op == 'd':
            if num < 0:
                num = (num*-1 // nums[idx+1]) * -1
            else:
                num //= nums[idx+1]
    if ans[0] == None or ans[0] > num:
        ans[0] = num
    if ans[1] == None or ans[1] < num:
        ans[1] = num

print(ans[1])
print(ans[0])