# 위장

def solution(clothes):
    from collections import Counter
    answer = 1
    dic = Counter(category for item, category in clothes)
    for key in dic.keys():
        answer *= (dic[key] + 1)
    answer -= 1
    return answer

# 의상의 카테고리에 맞춰서 딕셔너리를 생성함
# (의상의 카테고리)-(개수)의 key-value임
# (개수 + 1(의상을 입지 않는 경우)) * (개수 + 1) * ... - 1(아무것도 입지 않는 경우)가 answer임

# 1. dict.keys()
# -> 딕셔너리의 key들을 list로 가져오기 위해 딕셔너리 객체의 keys 메소드를 호출해야 함