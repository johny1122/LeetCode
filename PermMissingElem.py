# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def solution(A):
    if not A:
        return 1
    A.sort()
    for i, a in enumerate(A):
        if i + 1 != a:
            return i + 1
    return A[-1] + 1


if __name__ == '__main__':
    # print(solution([2,3,1,5]))
    # print(solution([1,5, 2,3]))
    print(solution([1,4, 2,3]))
    # print(solution([3,4,2,1,6]))
    # print(solution([1]))
    # print(solution([2]))
    # print(solution([]))
