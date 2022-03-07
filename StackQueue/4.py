# 주식 가격
def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        check = True
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                answer.append(count + 1)
                check = False
                break
        if check:
            answer.append(count)
    return answer

# 경우 1. price 하락을 만난 경우 -> break
# 경우 2. 끝까지 기능 경우 -> check = True