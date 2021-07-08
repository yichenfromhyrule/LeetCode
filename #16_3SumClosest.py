class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 1. Sort the nums list
        nums.sort()
        print(nums)
        result = sum(nums[:3])
        # 2. Go through each num in list, the target = target - num
        for i in range(0, len(nums)):
            checked_list = [False for j in range(len(nums))]
            curr_target = target - nums[i]
            left_key = i + 1
            right_key = len(nums) - 1

            while left_key < right_key and not checked_list[left_key] and not checked_list[right_key]:
                print("leftkey = %d, rightkey = %d, i = %d, sum = %d" % (
                left_key, right_key, i, nums[left_key] + nums[right_key] + nums[i]))
                curr_sum = nums[left_key] + nums[right_key]
                curr_result = curr_sum + nums[i]
                if abs(result - target) > abs(curr_result - target):
                    result = curr_result
                if curr_sum > curr_target:
                    right_key -= 1
                elif curr_sum == curr_target:
                    return target
                else:
                    left_key += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,2,1,-4]
    target = 1
    r= solution.threeSumClosest(nums, target)
    print(r)