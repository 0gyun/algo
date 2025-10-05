#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1213                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1213                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:29:42 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
# from itertools import permutations
input = sys.stdin.readline

def main():
    name = list(input().strip())
    sets = list(set(name))
    cnt = [name.count(a) for a in sets]
    odds = -1
    for c in range(len(cnt)):
        if cnt[c] % 2:
            if odds != -1:
                print("I'm Sorry Hansoo")
                return
            odds = c

    half_alphas = [sets[idx]*(cnt[idx]//2) for idx in range(len(sets))]
    half_alphas.sort()
    # perms = list(permutations(half_alphas, len(half_alphas))) # 얘가 메모리 다 잡아먹음

    if odds == -1:
        print(''.join(half_alphas) + ''.join(half_alphas[::-1]))
    else:
        print(''.join(half_alphas) + sets[odds] + ''.join(half_alphas[::-1]))

if __name__ == "__main__":
    main()