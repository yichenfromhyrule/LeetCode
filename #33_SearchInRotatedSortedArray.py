class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        else:
            # 1. Find the smallest value's position
            smallest_position = self.findRotated(nums, 0, len(nums) - 1)
            if smallest_position == 0:
                return self.findTarget(nums, target, 0, len(nums) - 1)
            else:
                # 2. Get the ascending list
                first_part = nums[:smallest_position]
                second_part = nums[smallest_position:]
                # 3. Get the target index
                first_index = self.findTarget(first_part, target, 0, len(first_part) - 1)
                second_index = self.findTarget(second_part, target, 0, len(second_part) - 1)
                if first_index != -1:
                    return first_index
                elif second_index != -1:
                    return len(first_part) + second_index
                else:
                    return -1

    def findRotated(self, nums, start, end):
        if end - start == 1:
            if nums[end] < nums[start]:
                return end
            else:
                return start
        else:  # 1. Means it has a rotated
            mid = (start + end) // 2
            if nums[start] < nums[mid]:  # 2. Means [mid, end] has rotated
                return self.findRotated(nums, mid, end)
            else:
                return self.findRotated(nums, start, mid)  # 3. Means [start, mid] has rotated

    def findTarget(self, original_nums, target, start, end):
        # print("I am checking index[%d] and [%d]"%(start, end))
        if end == start:
            return -1 if original_nums[start] != target else start
        elif end - start == 1:
            if original_nums[start] == target:
                return start
            elif original_nums[end] == target:
                return end
            else:
                return -1
        else:
            mid = (start + end) // 2
            if original_nums[mid] == target:
                return mid
            else:
                if original_nums[mid] > target:
                    return self.findTarget(original_nums, target, start, mid)
                else:
                    return self.findTarget(original_nums, target, mid, end)
