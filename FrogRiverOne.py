# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

def solution(X, A):
    if not A:
        return -1
    left_nums = {i: i for i in range(1, X + 1)}

    for i in range(len(A)):
        if A[i] in left_nums:
            left_nums.pop(A[i])
            if not left_nums:
                return i
    return -1


if __name__ == '__main__':
    # print(solution(5, [1,3,1,4,2,3,5,4]))
    # print(solution(4, [1,3,1,2,2,4,1]))
    # print(solution(2, [1,1,1,1,1,2]))
    # print(solution(2, [2]))
    # print(solution(1, [2]))
    # print(solution(1, [1]))
    print(solution(2, []))
