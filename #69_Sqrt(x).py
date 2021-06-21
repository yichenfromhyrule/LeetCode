class Solution(object):
    def findSqrt(self, start, end, x):
        mid = (start+end)//2
        if mid**2 <= x and (mid+1)**2 > x:
            return mid
        elif mid**2 > x:
            return self.findSqrt(start, mid, x)
        elif mid**2 < x:
            return self.findSqrt(mid, end, x)
        else:
            return mid
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        else:
            return self.findSqrt(0, x, x)

if __name__ == '__main__':
    s = Solution()
    x = 50
    r = s.mySqrt(x)
    print(r)