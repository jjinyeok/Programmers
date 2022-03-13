# 모의고사

def solution(answers):
    person1, person2, person3 = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    count = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == person1[i % 5]:
            count[0] += 1
        if answers[i] == person2[i % 8]:
            count[1] += 1
        if answers[i] == person3[i % 10]:
            count[2] += 1
    answer = []
    maxCount = max(count)
    for i in range(3):
        if maxCount == count[i]:
            answer.append(i + 1)
    return answer

# 순환주기마다 count를 세고 그에 따라 최대값을 가지는 index + 1을 return
