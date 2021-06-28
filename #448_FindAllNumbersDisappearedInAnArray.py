class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = [0 for i in range(len(nums))]
        for num in nums:
            hashmap[num-1]+=1
        result = []
        for i in range(len(hashmap)):
            if hashmap[i]==0:
                result.append(i+1)
        return result

if __name__ == '__main__':
    s = Solution()
    n = [1,2,4,2]
    r = s.findDisappearedNumbers(n)
    print(r)