# 베스트 앨범

def solution(genres, plays):
    answer = []
    dic = dict()
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [plays[i], [[plays[i], i]]]
        else:
            dic[genres[i]][0] += plays[i]
            dic[genres[i]][1].append([plays[i], i])
    
    results = []
    for key in dic.keys():
        results.append(dic[key])
    results.sort(key= lambda x: -x[0])
    
    for result in results:
        total, elements = result
        elements.sort(key= lambda x: (-x[0], x[1]))
        if len(elements) == 1:
            answer.append(elements[0][1])
        else:
            for i in range(2):
                answer.append(elements[i][1])

    return answer

# (장르)-([전체 재생 수, [[재생 수1, 인덱스1], [재생 수2, 인덱스2], ...]])의 key-value를 가지고 있는 딕셔너리 생성
# [전체 재생 수, [[재생 수1, 인덱스1], [재생 수2, 인덱스2], ...]]의 리스트를 생성
# 전체 재생 수 기준 내림차순으로 정렬 (lambda x: -x[0])
# 재생 수 기준 내림차순으로 요소들도 정렬 (lambda x: -x[0])
# 전체 재생 수와 각각의 재생 수에 따라 index가 answer로 append됨
# (이때, 재생 수가 같은 경우, lambda x: (-x[0], x[1])이었으므로 인덱스는 오름차순으로 정렬되었기 때문에 상관 없음)
