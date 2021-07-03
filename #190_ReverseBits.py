class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 1. convert n to binary
        str_n = str(bin(n).replace('0b', ''))
        pre_n = ''
        for i in range(32 - len(str_n)):
            pre_n += '0'
        str_n = pre_n + str_n

        # 2. compute the result
        result = 0
        for i in range(0, len(str_n)):
            result += (2 ** i) * int(str_n[i])

        return result
if __name__ == '__main__':
    s = Solution()
    n = '00000010100101000001111010011100'
    r = s.reverseBits(n)
    print(r)