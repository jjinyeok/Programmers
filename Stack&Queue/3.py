# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    for _ in range(bridge_length):
        bridge.append(0)
    truck_queue = deque()
    for truck_weight in truck_weights:
        truck_queue.append(truck_weight)

    truck_weights_sum = 0
    while True:
        truck_weights_sum -= bridge.pop()
        bridge.appendleft(0)
        if len(truck_queue) > 0:
            if truck_weights_sum + truck_queue[0] <= weight:
                bridge[0] = truck_queue.popleft()
                truck_weights_sum += bridge[0]
        answer += 1
        if truck_weights_sum == 0:
            break
    return answer

# bridge라는 list 생성 후, truck_weights_sum이라는 변수로 다리에 있는 트럭의 무게 합 체크
# truck_weights_sum에 새로운 트럭의 무게를 더해도 weight를 넘지 않는다면 bridge.appendleft(truck.popleft())
# weight를 넘는다면 bridge.appendleft(0)

# 1. truck_weights를 앞부터 하나씩 빼려고 큐를 생성해서 popleft()를 했었다.
# -> truck_weights에 reverse()를 사용하여 스택에서 pop()을 할 수 있다.
