# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

def solution(A):
    A.sort()

    for i in range(len(A)):
        if A[i] != i + 1:
            return 0
    return 1


if __name__ == '__main__':
    # print(solution([4, 1, 3, 2]))
    # print(solution([4, 1, 2]))
    # print(solution([4, 3 , 2]))
    # print(solution([1,2,3,4,5,6,7]))
    # print(solution([1,2,7,3,6,4,5]))
    print(solution([1]))