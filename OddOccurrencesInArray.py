# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort()
    for i in range(0, len(A) - 1, 2):
        if A[i] != A[i + 1]:
            return A[i]
    return A[-1]


if __name__ == '__main__':
    # print(solution([9,3,9,3,9,7,9]))
    # print(solution([1,7,3,9,7,3,4,9,1]))
    # print(solution([1]))
    # print(solution([1,2,1]))
    # print(solution([1,2,1,2,3]))
    # print(solution([1,2,1,2,3]))
    # print(solution([1,3,2,1,3]))
    print(solution([155]))
