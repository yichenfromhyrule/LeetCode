class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        else:
            prime_list = [2]
            for i in range(2, n):
                is_prime = True
                for prime_num in prime_list:
                    if i % prime_num == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_list.append(i)
            print(prime_list)
            return len(prime_list)


if __name__ == '__main__':
    s = Solution()
    n = 160
    r= s.countPrimes(n)
    print(r)