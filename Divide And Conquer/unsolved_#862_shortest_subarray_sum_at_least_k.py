import numpy as np
def shortestSubarray(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 0. Sort the array num
        nums.sort(reverse=True)
        nums_copy = nums
        # 1. Check the largest element's value is larger than k
        if nums[0]>=k:
            return 1
        elif sum(nums)<k:
            return -1
        else:
            # 2. Get the length of first result(Maybe not the shortest one)
            first_result = findsub(nums, k)
            first_sub = nums[0:first_result]
            final_result = findshortest(first_sub, k)
            if sum(nums[0:final_result])<k:
                return final_result+1
            else:
                return final_result


def findsub(nums,k):
        sub_sum = 0
        sub_len = 0
        while sub_sum < k:
            sub_sum += sum(nums[0: len(nums) // 2])
            sub_len += len(nums) // 2
            nums = nums[len(nums) // 2: len(nums)]
        print("1:", sub_len)
        return sub_len

def findshortest(nums, k):
        sub_sum = sum(nums)
        sub_len = len(nums)
        while sub_sum > k:
            sub_sum -= sum(nums[len(nums)//2: len(nums)])
            sub_len -= len(nums) // 2
            nums = nums[0:len(nums)//2]
        print("2:", sub_len)
        return sub_len

a = [2,-1,2]
b = 3
r = shortestSubarray(a,b)
print("R: ", r)



