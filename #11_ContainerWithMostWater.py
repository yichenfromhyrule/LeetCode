class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left_key = 0
        right_key = 0
        maxarea_key = 0
        for i in range(1, len(height)):
            curr_area = (i-left_key) * min(height[i], height[left_key])
            if curr_area > area :
                area = curr_area
                if height[i] <= height[left_key]:
                    right_key = i
                else:
                    if height[i] >= height[left_key] * (i-left_key):
                        left_key = i
        print("left_key = %d, right_key = %d, area = %d"%(left_key, right_key, area))
        return area
if __name__ == '__main__':
    s = Solution()
    height = [1,2,4,3]
    r= s.maxArea(height)
    print(r)