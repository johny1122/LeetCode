# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):
    b = int(bin(N)[2:])
    if '0' not in str(b) or '1' not in str(b):
        return 0
    first_found = True
    max_gap = 0
    curr_gap = 0
    while b != 0:
        remain = b % 10
        if remain == 1:
            if first_found:
                first_found = False
                continue
            if max_gap < curr_gap:
                max_gap = curr_gap
                curr_gap = 0
        elif not first_found:
            curr_gap += 1
        b //= 10

    return max_gap


if __name__ == '__main__':
    print(solution(1041))