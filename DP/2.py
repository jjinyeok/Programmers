# 정수 삼각형

def solution(triangle):
    answer = triangle[0][0]
    results = triangle * 1
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                results[i][j] = results[i - 1][j] + triangle[i][j]
                if results[i][j] > answer:
                    answer = results[i][j]
            elif j == len(triangle[i]) - 1:
                results[i][j] = results[i - 1][j - 1] + triangle[i][j]
                if results[i][j] > answer:
                    answer = results[i][j]
            else:
                A = triangle[i - 1][j - 1] + triangle[i][j]
                B = triangle[i - 1][j] + triangle[i][j]
                if A > B:
                    results[i][j] = A
                else:
                    results[i][j] = B
                if results[i][j] > answer:
                    answer = results[i][j]
    return answer

# 모든 삼각형의 값 results[i][j]에 대하여 최대값을 구해줌
# 경우1. j == 0인 경우, results[i - 1][j] + triangle[i][j]
# 경우2. j == len(results[i]) - 1인 경우, results[i - 1][j - 1] + triangle[i][j]
# 경우3. 나머지 경우, results[i - 1][j] + triangle[i][j], results[i - 1][j - 1] + triangle[i][j] 중 큰 값

# 1. max함수
# results[i - 1][j] + triangle[i][j], results[i - 1][j - 1] + triangle[i][j] 중 큰 값은 조건문이 아니라 max함수를 사용하여 해결이 가능함
# 2. 굳이 results라는 triangle과 같은 리스트를 만들지 않고도 해결이 가능했음
# 3. 굳이 하나씩 answer를 체크해주기 보다 max(results[-1])의 값이 answer이 됨