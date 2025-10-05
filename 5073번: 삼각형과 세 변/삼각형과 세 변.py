#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5073                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: yklee1130 <boj.kr/u/yklee1130>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5073                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 17:19:05 by yklee1130     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

if __name__ == "__main__":
    while True:
        a, b, c = map(int, input().split())
        if a+b+c == 0:
            break
        a, b, c = sorted([a, b, c])
        if a == b == c:
            print("Equilateral")
        elif a + b <= c:
            print("Invalid")
        elif a == b or b == c:
            print("Isosceles")
        else:
            print("Scalene")
    exit(0)