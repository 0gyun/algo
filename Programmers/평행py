"""
https://school.programmers.co.kr/learn/courses/30/lessons/120875
문제 설명
점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

제한사항
dots의 길이 = 4
dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
0 ≤ x, y ≤ 100
서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.

입출력 예
dots	result
[[1, 4], [9, 2], [3, 8], [11, 6]]	1
[[3, 5], [4, 1], [2, 4], [5, 10]]	0

입출력 예 설명

입출력 예 #1
점 [1, 4], [3, 8]을 잇고 [9, 2], [11, 6]를 이으면 두 선분은 평행합니다.

입출력 예 #2
점을 어떻게 연결해도 평행하지 않습니다.
"""
def solution(dots):
    answer = 0
    # 두 점의 조합은 다음과 같다.
    comb = [[0, 1, 2, 3],
            [0, 1, 3, 2], 
            [0, 2, 1, 3], 
            [0, 2, 3, 1], 
            [0, 3, 1, 2], 
            [0, 3, 2, 1]
            ]
    xs = []
    ys = []
    for dot in dots:
       xs.append(dot[0])
       ys.append(dot[1])

    for c in comb:
        # 두 점의 x변화량과 y변화량을 구한다.
        dx1 = xs[c[1]]-xs[c[0]]
        dy1 = ys[c[1]]-ys[c[0]]
        
        dx2 = xs[c[3]]-xs[c[2]]
        dy2 = ys[c[3]]-ys[c[2]]

        # x변화량과 y변화량이 같은지 확인한다.
        if dx1 == dx2 and dy1 == dy2:
            return 1
        if dx1 != 0 and dx2 != 0:
            if dy1/dx1 == dy2/dx2:
                return 1
    
    return answer


# main start!
# dots = [[1, 4], [9, 2], [3, 8], [11, 6]]		#TC no.1
dots = 	[[3, 5], [4, 1], [2, 4], [5, 10]]		#TC no.2
print(solution(dots)) 
# main end!