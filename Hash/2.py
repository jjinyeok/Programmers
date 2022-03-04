# 전화번호 목록

def solution(phone_book):
    answer = True
    result = dict()
    for phone_num in phone_book:
        tmp = ''
        for i in range(len(phone_num)):
            tmp += phone_num[i]
            if tmp in result:
                result[tmp] += 1
            else:
                result[tmp] = 1
    for phone_num in phone_book:
        if result[phone_num] > 1:
            answer = False
            break
    return answer

# phone_num에서 모든 접두어가 될 수 있는 경우를 딕셔너리에 넣음
# (접두어가 될 수 있는 번호)-(나온 횟수)가 key-value가 됨
# 다시 phone_book에서 phone_num을 돌리며
# 딕셔너리 (phone_num)의 value가 2 이상인 경우 answer=False 아닌경우 answer=True임
# (1인 경우 본인 한번만 나온 경우이기 때문임)
