#기능 개발
from collections import deque

def solution(progresses, speeds):
    queue = deque()
    for i in range(len(progresses)):
        queue.append([progresses[i], speeds[i]])

    answer = []
    while queue:
        for i in range(len(queue)):
            queue[i][0] += queue[i][1]
        count = 0
        while True:
            if len(queue) > 0 and queue[0][0] >= 100:
                queue.popleft()
                count += 1
            else:
                if count != 0:
                    answer.append(count)
                break
    return answer

# popleft()를 사용하여 시간을 줄이고 싶어서 deque를 사용함
# queue에 [progress, speed]를 짝지어 넣었음
# 모든 progress(queue[i][0])에 speed(queue[i][1])를 더하고
# queue[0][0] 즉 당장 배포되어야 할 기능을 항상 검사함

# 1. Index error가 떴을때는 조건문을 잘 세웠는지 확인해야 함
# -> programmers는 디버깅하기 어려움(print문보다 에러문이 먼저 나옴)
