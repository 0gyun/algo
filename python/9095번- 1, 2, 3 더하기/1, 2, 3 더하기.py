#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9095                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9095                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:38:09 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

def one_two_three(num):
    if num <= 3:
        if num <= 0:
            return 0
        if num <= 2:
            return num
        return 4

    return one_two_three(num - 3) + one_two_three(num - 2) + one_two_three(num - 1)
        

t = int(input())
for _ in range(t):
    n = int(input())
    print(one_two_three(n))