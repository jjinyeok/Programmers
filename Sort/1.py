# K번째 수

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i - 1:j])[k - 1])
    return answer

# 1. lambda도 사용할 수 있으면 사용해야겠다.
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
