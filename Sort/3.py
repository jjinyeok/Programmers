# H-Index

def solution(citations):
    answer = 0
    citations.sort()
    while True:
        count = 0
        for citation in citations:
            if citation >= answer:
                count += 1
        if count < answer:
            break
        answer += 1
    return answer - 1

# 현재 O(N^2)짜리 코드임
# 구현은 간단함. answer를 1씩 증가하며 
# answer보다 작은 논문 인용횟수를 만나면 break
# 이때 answer - 1을 return함

# 1.
# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0
# -> 남은 함수를 기준으로 생각한다면 O(N)으로도 풀 수 있는 문제였음...
