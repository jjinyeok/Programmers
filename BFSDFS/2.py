# 네트워크

from collections import deque

def solution(n, computers):
    answer = 0
    network = [0] * n
    for i in range(n):
        if network[i] == 0:
            answer += 1
            queue = deque()
            queue.append(i)
            while queue:
                now = queue.popleft()
                network[now] = answer
                for i in range(len(computers[now])):
                    if computers[now][i] == 1 and network[i] == 0:
                        network[i] = answer
                        queue.append(i)
    return answer

# computer수 만킁의 배열 network 생성
# computer수 만큼 network를 돌리며 network = 0인 곳에서 bfs 탐색
# 각각의 network 배열에 몇 번째 network인지 기록
# 마지막 네트워크의 숫자가 결국 정답일 것임 (네트워크의 숫자는 몇번째 네트워크인지를 기록하기 때문)
