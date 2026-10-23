#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1920                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1920                           #+#        #+#      #+#     #
#    Solved: 2025/10/09 21:15:20 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def binary_search(numbers, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return 0
    if numbers[mid] == target:
        return 1
    if numbers[mid] > target:
        return binary_search(numbers, target, start, mid-1)
    else:
        return binary_search(numbers, target, mid+1, end)

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num > A[-1] or num < A[0]:
        print(0)
    else:
        print(binary_search(A, num, 0, N-1))