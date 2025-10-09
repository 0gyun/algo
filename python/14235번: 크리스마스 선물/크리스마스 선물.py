#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14235                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14235                          #+#        #+#      #+#     #
#    Solved: 2025/10/09 22:32:40 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
gifts=[]
for _ in range(n):
    stop = list(map(int,input().split()))
    if stop[0] == 0:
        print(gifts.pop() if gifts else -1)
    else:
        new_gifts = stop[1:]
        gifts.extend(new_gifts)
        gifts.sort()