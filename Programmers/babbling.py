"""
https://school.programmers.co.kr/learn/courses/30/lessons/120956
문제 설명
머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ babbling의 길이 ≤ 100
1 ≤ babbling[i]의 길이 ≤ 15
babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.
즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가 한 번씩만 등장합니다.
문자열은 알파벳 소문자로만 이루어져 있습니다.
입출력 예
babbling	result
["aya", "yee", "u", "maa", "wyeoo"]	1
["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	3
입출력 예 설명
입출력 예 #1

["aya", "yee", "u", "maa", "wyeoo"]에서 발음할 수 있는 것은 "aya"뿐입니다. 따라서 1을 return합니다.
입출력 예 #2

["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]에서 발음할 수 있는 것은 "aya" + "ye" = "ayaye", "ye", "ye" + "ma" + "woo" = "yemawoo"로 3개입니다. 따라서 3을 return합니다.
유의사항
네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정합니다. 예를 들어 "woowo"는 "woo"는 발음할 수 있지만 "wo"를 발음할 수 없기 때문에 할 수 없는 발음입니다.

"""
def solution(babbling):
    answer = 0
    for words in babbling:
        if len(words) == 1 or len(words) > 10: # 조카가 발음할 수 있는 최소 단어는 2자 이상, 모든 단어를 한번씩 발음하면 최대 10자여서 예외처리
            continue
        words = words.replace("aya", " ", 1) # 예를 들어 wayaoo를 w oo로 바꾸게 되면 후에 woo를 발음할 수 있다고 판단 안함.
        words = words.replace("ye", " ", 1)
        words = words.replace("woo", " ", 1)
        words = words.replace("ma", " ", 1)
        words = words.replace(" ","") # 빈칸으로 치환한 것들 제거.
        if words == "": # 다른 단어가 있다면 조카가 말할 수 없는 것들.
            answer += 1
    return answer


# main start!

babbling = ["aya", "yee", "u", "maa", "wyeoo"]		#TC no.1
#babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]		#TC no.2
print(solution(babbling)) 

# main end!