class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left_key = 0
        right_key = len(height) - 1
        while left_key < right_key:
            min_key = min(height[left_key], height[right_key])
            curr_area = min_key * (right_key - left_key)
            if curr_area > area:
                area = curr_area
            if min_key == height[left_key]:
                left_key += 1
            else:
                right_key -= 1
        return area
if __name__ == '__main__':
    s = Solution()
    height = [4,3,2,1,4]
    r= s.maxArea(height)
    print(r)