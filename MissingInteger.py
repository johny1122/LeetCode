# https://app.codility.com/demo/results/trainingRJK7Q4-J94/

def solution(A):
    A.sort()
    A = [a for a in A if a > 0]

    if not A or A[0] > 1:
        return 1

    for i in range(len(A) - 1):
        if A[i + 1] - A[i] > 1:
            return A[i] + 1
    return A[-1] + 1


if __name__ == '__main__':
    # print(solution([1,4,2,7,8]))
    # print(solution([2,4,2,7,8]))
    # print(solution([3,4,3,7,8]))
    # print(solution([-1, -4, 1, 7, 8,2,7,3,5,8]))
    # print(solution([1, 3, 6, 4, 1, 2]))
    # print(solution([1,2,3]))
    print(solution([-10, -33]))
    # print(solution([1,4,2,7,8]))
    # print(solution([-1,1,-5,-3]))

