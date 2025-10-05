#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16173                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16173                          #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:16:49 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline
def move(N, game_map, y, x):
    print(f"Now : ({x}, {y})")
    if x >= N or y >= N:
        return 0
    

    if game_map[y][x] == -1:
        return 1
    elif game_map[y][x] == 0:
        return 0
    
    print(f"To : ({x}, {y+game_map[y][x]})")
    down = move(N, game_map, y+game_map[y][x], x)
    print(f"To : ({x+game_map[y][x]}, {y})")
    right = move(N, game_map, y, x+game_map[y][x])
    return right + down        
    

N = int(input())
game_map = []
for _ in range(N):
    data = list(map(int, input().split()))
    row = [d for d in data]
    game_map.append(row)
clear = move(N, game_map, 0, 0)

ans = "HaruHaru" if clear > 0 else "Hing"
print(ans)