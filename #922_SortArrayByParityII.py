class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        result = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        for even_item, odd_item in zip(even, odd):
            result += [even_item, odd_item]
        return result