# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

def solution(X, Y, D):
    distance = Y - X
    number_of_jumps = distance // D
    if distance % D > 0:
        return number_of_jumps + 1
    return number_of_jumps


if __name__ == '__main__':
    # print(solution(10, 85, 30))
    print(solution(10, 31, 10))