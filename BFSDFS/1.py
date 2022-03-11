# 타겟 넘버

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([numbers[0] * (-1), 0])
    length = len(numbers)
    while queue:
        value, count = queue.popleft()
        if value == target and count == length - 1:
            answer += 1
        if count < length - 1:
            queue.append([value + numbers[count + 1], count + 1])
            queue.append([value - numbers[count + 1], count + 1])
    return answer

# bfs를 사용해서 [현재 값, count]로 모두 탐색
# count가 numbers의 길이보다 하나 작고(count 0부터 시작했기 때문)
# 그때 현재 값이 target과 같다면 answer += 1

# 1. dfs로 푼 사람들이 많았음
# def solution(numbers, target):
#     if not numbers and target == 0:
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
# target값을 현재 numbers만큼 줄여서 재귀로 솔루션을 완성해 나갔음
# 재귀를 사용하는 것보다는 queue(bfs) or stack(dfs)를 사용하는 것을 좋아하는데 차피 모든 경우를 도는데에서 시간은 비슷하게 걸릴거라 생각함