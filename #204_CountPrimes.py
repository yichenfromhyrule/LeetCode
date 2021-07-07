class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        else:
            hashmap = [0 for i in range(n)]
            for i in range(2, n):
                number = i
                while i * number < n:
                    if hashmap[i*number] == 0:
                        hashmap[i*number] = 1
                    number += 1
            count = -2
            for num in hashmap:
                if num == 0:
                    count += 1
            return count


if __name__ == '__main__':
    s = Solution()
    n = 10
    r= s.countPrimes(n)
    print(r)