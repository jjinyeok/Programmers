# 단어 변환

from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append(begin)
    length = len(begin)
    distance = {begin: 0}
    while queue:
        now = queue.popleft()
        if now == target:
            return distance[now]
        for word in words:
            check = 0
            for i in range(length):
                if word[i] != now[i]:
                    check += 1
            if check == 1 and word not in distance:
                distance[word] = distance[now] + 1
                queue.append(word)
    return 0

# 글자마다 딕셔너리 해시 구조로 bfs 진행함