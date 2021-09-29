class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = len(arr)
        odd_list = [(2 * i + 1) for i in range(l // 2)]
        if l % 2 == 1:
            odd_list.append(l)

        r = 0
        for j in range(l):
            for o in odd_list:
                need = o - 1
                left_key = 0 if (j - need) <= 0 else (j - need)
                right_key = (l - 1) if (j + need) >= l else (j + need)
                distance = right_key - left_key + 2 - o
                if distance > 0:
                    r += distance * arr[j]

        return r

