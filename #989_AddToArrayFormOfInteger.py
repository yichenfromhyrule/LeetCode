class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        str_num = ""
        for n in num:
            str_num += str(n)
        result = int(str_num) + k
        str_result = str(result)
        output = []
        for s in str_result:
            output.append(int(s))
        return output