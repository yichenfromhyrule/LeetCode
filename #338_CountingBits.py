import math
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0, 1]
        if n <= 1:
            return result[:n + 1]
        else:
            sqrt_i = 0
            for i in range(2, n + 1):
                sqrt_i = math.log(i, 2)
                if sqrt_i == int(sqrt_i):
                    sqrt_i = int(sqrt_i)
                    result.append(1)
                else:
                    sqrt_i = int(sqrt_i)
                    result.append(1 + result[i - 2 ** sqrt_i])
        return result


if __name__ == '__main__':
    s = Solution()
    n = 2
    r = s.countBits(n)
    print(r)