# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A, K):
    if K == len(A) or not A:
        return A

    for k in range(K):
        save_last = A[-1]
        for i in range(len(A) - 2, -1, -1):
            A[i + 1] = A[i]
        A[0] = save_last
    return A


if __name__ == '__main__':
    # print(solution([1,2,3,4], 3))
    # print(solution([1,2,3,4], 4))
    # print(solution([1, 2, 2, 3, 3, 4, 5, 6, 7], 1))
    # print(solution( [3, 8, 9, 7, 6], 1))
    # print(solution( [3, 8, 9, 7, 6], 3))
    # print(solution( [0,0,0], 1))
    print(solution( [], 1))
