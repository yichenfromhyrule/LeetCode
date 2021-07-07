class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        dp = [0 for i in range(len(height))]
        left = 0
        right = 0
        maxheight = 0

        # 1. Calculate the area between [x,y]
        for i in range (1, len(height)):
            # 2.a. [left, current_i]
            a_area = (i - left) * (min(height[i], height[left]))
            # 2.b. [max(height[:i-1], current_i]
            b_area = (i - maxheight) * (min(height[i], height[maxheight]))
            # 2.c. [right, current_i]
            c_area = (i - right) * (min(height[i], height[right]))
            #print("left = %d, right = %d, a_area=%d, b_area = %d, c_area = %d"%(left, right, a_area, b_area, c_area))
            curr_area = max(a_area, b_area, c_area, dp[i-1])
            # 3. Update the left and right
            if curr_area == b_area:
                left = maxheight
                right = i
            elif curr_area == a_area:
                right = i
            elif curr_area == curr_area:
                left = right
                right = i
            # 4. Update the maxheight:
            maxheight = i if height[i] > height[maxheight] else maxheight
            # 5. Update dp list and area
            dp[i] = curr_area
            area = curr_area if curr_area > area else area

        print(dp)

        return area
if __name__ == '__main__':
    s = Solution()
    height = [1,2,4,3]
    r= s.maxArea(height)
    print(r)