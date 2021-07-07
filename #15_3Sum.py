class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 3:
            return result
        else:
            for i in range(0, len(nums)):
                r = [nums[i]]
                new_nums = nums[i+1:]
                hashmap = {}
                target = 0 - nums[i]
                for j in range(0, len(new_nums)):
                    if hashmap.get(new_nums[j])!=None:
                        r += [target-new_nums[j], new_nums[j]]
                        r.sort()
                        if r not in result:
                            result.append(r)
                        r = [nums[i]]
                        del hashmap[new_nums[j]]
                    else:
                        if hashmap.get(new_nums[j])==None:
                            hashmap[target-new_nums[j]] = j

            return result


if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    r= s.threeSum(nums)
    print(r)