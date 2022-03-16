# 가장 먼 노드

from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    visited = [0] * (n + 1)
    queue = deque()
    queue.append(1)
    visited[1] = 1
    while queue:
        now = queue.popleft()
        for element in graph[now]:
            if visited[element] == 0:
                visited[element] = visited[now] + 1
                queue.append(element)
    m = max(visited)
    for i in range(1, n + 1):
        if visited[i] == m:
            answer += 1
    return answer

# 평범한 BFS 문제