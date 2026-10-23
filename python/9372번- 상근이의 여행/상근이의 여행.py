#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9372                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9372                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:38:39 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

def travel(start, lines, visited, count):
    departures = lines[start]
    visited.append(start)
    for d in departures:
        if d not in visited:
            count = travel(d, lines, visited, count+1)
    return count

test_cases = int(input())
for _ in range(test_cases):
    countries, planes = input().split()
    lines = {}
    for country in range(1, int(countries)+1):
        lines[str(country)] = []
    for _ in range(int(planes)):
        a, b = input().split()
        lines[a].append(b)
        lines[b].append(a)

    count = travel(countries, lines, [], 0)
    print(count)
