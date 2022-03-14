# 등굣길

def solution(m, n, puddles):
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for puddleX, puddleY in puddles:
        graph[puddleY - 1][puddleX - 1] = -1
    graph[0][0] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                if i == 0 and j != 0:
                    if graph[i][j - 1] == -1:
                        graph[i][j] = 0
                    else:
                        graph[i][j] = graph[i][j - 1]
                elif i != 0 and j == 0:
                    if graph[i - 1][j] == -1:
                        graph[i][j] = 0
                    else:
                        graph[i][j] = graph[i - 1][j]
                else:
                    if graph[i - 1][j] != -1 and graph[i][j - 1] != -1:
                        graph[i][j] = (graph[i - 1][j] + graph[i][j - 1]) % 1000000007
                    elif graph[i - 1][j] != -1 and graph[i][j - 1] == -1:
                        graph[i][j] = graph[i - 1][j]
                    elif graph[i - 1][j] == -1 and graph[i][j - 1] != -1:
                        graph[i][j] = graph[i][j - 1]
                    else:
                        graph[i][j] = 0
    return graph[n - 1][m -1]

# 리팩토링 한다면 더 깔끔한 코드를 만들 수 있겠지만 모든 경우를 가장 잘 보인 것 같아서 냅둠
# graph[i][j] 기준 크게 3가지 경우가 있음
# 1) i == 0: if) graph[i][j - 1] == -1 -> 0 else) -> graph[i][j - 1]
# 2) j == 0: if) graph[i - 1][j] == -1 -> 0 else) -> graph[i - 1][j]
# 3) i != 0 and j != 0:
#    if) graph[i - 1][j] == -1 and graph[i][j - 1] == -1 -> 0
#    elif) graph[i - 1][j] == -1 -> graph[i][j - 1]
#    elif) graph[i][j - 1] == -1 -> graph[i - 1][j]
#    else) graph[i][j - 1] + graph[i - 1][j]

# 1. 모든 경우의 수를 생각했어야 하는데, 가장자리(i == 0 or j == 0)에 물웅덩이가 있을 수 있다는 생각을 잠시 놓침
# 2. 굳이 graph의 크기를 m * n으로 지정해둘 필요 없이
#     -> (m + 1) * (n + 1)로 지정해뒀다면, 가장자리를 따로 계산하는 생각을 할 필요 없이 모든 경우를 대각선 방향으로 해결 할 수 있었음
#     -> 현재 가장자리 경우, 대각선을 배제하고 좌, 상의 경우를 따라 계산해주고 있으나 (m + 1) * (n + 1) 지도에 해당하지 않는 경우를 0으로 지정한다면
#     -> 모두가 똑같은 방식으로 대각선을 기준으로 하여 계산이 가능함
# 3. 2022 상반기 skict 3번 문제와 비슷한 부분이 있음 => 더 공부하면 좋을듯
