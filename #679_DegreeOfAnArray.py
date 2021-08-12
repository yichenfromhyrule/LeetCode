class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = [i]
            else:
                hashmap[nums[i]].append(i)
        nums.sort()
        most_nums = []
        max_size = 0
        checking = nums[0]
        curr_size = 1
        for j in range(1, len(nums)):
            num = nums[j]
            if num == checking:
                curr_size += 1
            else:
                if curr_size > max_size:
                    max_size = curr_size
                    most_nums = [checking]
                elif curr_size == max_size:
                    most_nums.append(checking)
                checking = num
                curr_size = 1
        if curr_size > max_size:
            max_size = curr_size
            most_nums = [checking]
        elif curr_size == max_size:
            most_nums.append(checking)
        result = []
        for most_num in most_nums:
            result.append(hashmap[most_num][-1] - hashmap[most_num][0] + 1)
        return min(result)