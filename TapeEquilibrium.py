# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])

    minimal_diff = 0
    first = True
    left_sum = 0
    list_sum = sum(A)
    for p in range(1, len(A)):
        left_sum += A[p - 1]
        curr_abs_diff = abs(left_sum - (list_sum - left_sum))
        if first:
            minimal_diff = curr_abs_diff
            first = False
            continue
        if curr_abs_diff < minimal_diff:
            minimal_diff = curr_abs_diff

    return minimal_diff


if __name__ == '__main__':
    # print(solution([3,1,2,4,3]))
    # print(solution([1,2,3,4]))
    # print(solution([-5, -100]))
    # print(solution([-10, 10]))
    # print(solution([1, 1, 1]))
    print(solution([1, 1, 1, 1]))
