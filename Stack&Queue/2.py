#프린터
from collections import deque

def solution(priorities, location):
    queue = deque()
    for i in range(len(priorities)):
        queue.append([priorities[i], i])

    results = []
    while queue:
        now = queue.popleft()
        check = True
        for i in range(len(queue)):
            if now[0] < queue[i][0]:
                queue.append(now)
                check = False
                break
        if any(now[0] < a[0] for a in queue):
            queue.append(now)
            check = False
        if check:
            results.append(now)

    for i in range(len(results)):
        if location == results[i][1]:
            answer = i + 1
    return answer

# [우선순위, 인덱스] 형태로 queue에 넣음
# popleft() 한 값이 남은 queue의 우선순위들보다 크다면 answer에 append
# popleft() 한 값이 남은 queue의 어떠한 우선순위 보다 작다면 queue에 append

# 1. any함수
# -> any(iterableValue): iterableValue 중 하나라도 True일 경우 True return
# -> ex) 
# for i in range(len(queue)):
#     if now[0] < queue[i][0]:
#         queue.append(now)
#         check = False
#         break
# ->
# if any(now[0] < tmp[0] for tmp in queue):
#     queue.append(now)
#     check = False
