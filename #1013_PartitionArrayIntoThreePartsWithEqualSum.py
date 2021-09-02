class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s_arr = sum(arr)
        if s_arr % 3 != 0:
            return False
        else:
            s_t = s_arr // 3
            s_1 = 0
            count = 0
            for i in range(0, len(arr)):
                s_1 += arr[i]
                if s_1 == s_t:
                    count += 1
                    s_1 = 0
            return count >= 3