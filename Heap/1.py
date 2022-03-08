# 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True:
        if len(scoville) == 1:
            answer = -1
            break
        if scoville[0] >= K:
            break
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + second * 2
        heapq.heappush(scoville, mixed)
        answer += 1
    return answer

# 우선순위가 스코빌 지수인 힙을 만들고 사용함

# 1. 힙으로 변환 heapfy(list): list를 힙으로 만듬 (O(logN))
# -> scovile.sort() -> heapfy(scovile)
# 2. 최대힙: heappush(list, (-num, num)):
# -> 대신 heappop()을 사용할때, heappop(heap)[1]로 값을 꺼내와야 함
