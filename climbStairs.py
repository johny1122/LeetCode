import math


class Solution:
    def climbStairs(self, n: int) -> int:
        ways_num = 1  # include all 1s
        for i in range(math.ceil(n / 2), n):
            ways_num += math.comb(i, n % i)

        return ways_num


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(5))
    print(s.climbStairs(6))
