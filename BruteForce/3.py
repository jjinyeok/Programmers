# 카펫

import sys
sys.setrecursionlimit(987654321)

def solution(brown, yellow):
    answer = backtracking(1, 1, brown, yellow)
    return answer

def backtracking(x, y, brown, yellow):
    if x * y == yellow and 2 * x + 2 * y + 4 == brown:
        return [x + 2, y + 2]
    if x == y:
        return backtracking(x + 1, 1, brown, yellow)
    else:
        return backtracking(x, y + 1, brown, yellow)

# (yellow 가로, yellow 세로)의 경우는 (1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3), (4, 1), ...
# 와 같은 식으로 진행됨 (가로 >= 세로이므로)
# 백트래킹을 사용해서 x * y == yellow && (x + 2) * (y + 2) - x * y == brown일 때
# [brown 가로, brown 세로] 값을 return
