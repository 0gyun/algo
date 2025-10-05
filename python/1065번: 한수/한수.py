#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1065                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1065                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:27:47 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

n = int(input())
count = 0

for i in range(1, n+1):
    if i < 100:
        count += 1
    else:
        digits = list(map(int, str(i)))
        is_ans = True
        for k in range(2, len(digits)):
            if digits[k-1] - digits[k-2] != digits[k]-digits[k-1]:
                is_ans = False
                break
        if is_ans:
            count += 1

print(count)