# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

def solution(N, A):
    curr_max = 0
    result = [0] * N

    for a in A:
        if 1 <= a <= N:
            result[a-1] += 1
            if curr_max < result[a-1]:
                curr_max = result[a-1]
        elif a == N+1:
            result = [curr_max] * N

    return result


if __name__ == '__main__':
    # print(solution(5, [3,4,4,6,1,4,4]))
    # print(solution(5, [3,6,2,1]))
    print(solution(5, [1,6,1,1,1,1,1]))