def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    center2 = {1: 1, 2: 0, 3: 1, 4: 2, 5: 1, 6: 2, 7: 3, 8: 2, 9: 3, 0: 3, '*': 4, '#': 4}
    center5 = {1: 2, 2: 1, 3: 2, 4: 1, 5: 0, 6: 1, 7: 2, 8: 1, 9: 2, 0: 2, '*': 3, '#': 3}
    center8 = {1: 3, 2: 2, 3: 3, 4: 2, 5: 1, 6: 2, 7: 1, 8: 0, 9: 1, 0: 1, '*': 2, '#': 2}
    center0 = {1: 4, 2: 3, 3: 4, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 2, 0: 0, '*': 1, '#': 1}
    left_now = '*'
    right_now = '#'
    for number in numbers:
        if number in left:
            left_now = number
            answer += 'L'
        elif number in right:
            right_now = number
            answer += 'R'
        else:
            if number == 2:
                if center2[left_now] < center2[right_now]:
                    left_now = number
                    answer += 'L'
                elif center2[right_now] < center2[left_now]:
                    right_now = number
                    answer += 'R'
                else:
                    if hand == 'left':
                        left_now = number
                        answer += 'L'
                    elif hand == 'right':
                        right_now = number
                        answer += 'R'
            elif number == 5:
                if center5[left_now] < center5[right_now]:
                    left_now = number
                    answer += 'L'
                elif center5[right_now] < center5[left_now]:
                    right_now = number
                    answer += 'R'
                else:
                    if hand == 'left':
                        left_now = number
                        answer += 'L'
                    elif hand == 'right':
                        right_now = number
                        answer += 'R'
            elif number == 8:
                if center8[left_now] < center8[right_now]:
                    left_now = number
                    answer += 'L'
                elif center8[right_now] < center8[left_now]:
                    right_now = number
                    answer += 'R'
                else:
                    if hand == 'left':
                        left_now = number
                        answer += 'L'
                    elif hand == 'right':
                        right_now = number
                        answer += 'R'
            elif number == 0:
                if center0[left_now] < center0[right_now]:
                    left_now = number
                    answer += 'L'
                elif center0[right_now] < center0[left_now]:
                    right_now = number
                    answer += 'R'
                else:
                    if hand == 'left':
                        left_now = number
                        answer += 'L'
                    elif hand == 'right':
                        right_now = number
                        answer += 'R'
    return answer