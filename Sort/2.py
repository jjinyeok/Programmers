# 가장 큰 수

def solution(numbers):
    a = 0
    for number in numbers:
        if a > 0:
            break
        a += number
    if a == 0:
        return '0'
    strings = list(map(str, numbers))
    strings.sort(reverse=True, key=lambda x: x*3)
    answer = ''.join(strings)
    return answer

# 실패
# 1. '1', '12', '112'를 정렬한다면,'121212' > '112112112' > '111' 과같이 문자열 * 3을 하여 정렬하는 아이디어를 도출해내지 못한 패착
# 2. lambda식을 사용해 정렬하면 더 편했을텐데 그 생각을 잊고 있었음
# -> 정렬 문제에서 lambda식을 사용할 수도 있다는 사실을 잊지말자
# 3. 0만 여러번 들어왔을 경우
# -> '00000'과 같은 형식으로 return되기 때문에, 예외처리를 해줘야하는데 이 부분을 놓쳤음
