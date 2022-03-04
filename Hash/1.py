# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    dic = dict()
    for p in participant:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    for c in completion:
        dic[c] -= 1
    for p in participant:
        if dic[p] == 1:
            answer = p
    return answer

# 참가자 중 1명을 제외하고 완주 하였기 때문에 (참가자의 이름)-(참가자의 수) key-value의 딕셔너리 생성
# 딕셔너리에서 완주자 만큼을 빼어야 하므로 key가 완주자 이름인 경우 value 값에서 1을 뺌
# 딕셔너리에서 단 하나의 경우에서만 key: 1일 것이고, 이때 key가 answer임

# 1. dic[key] = value
# -> list의 append와는 다르게 dic에 key-value를 추가하는 방법임
# 2. collection의 Counter 객체(데이터 개수를 셀 때 유용함)
# -> Counter(iterator): iterator 요소들의 개수를 세어주고 Counter 객체로 반환
# -> ex) Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ... , 'd': 1}) = Counter('hello world')
# 3. Counter 객체끼리 뺄셈이 가능함
