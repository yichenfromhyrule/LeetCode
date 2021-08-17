class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        record = [-1] * len(s)
        for i in range(0, len(s)):
            if s[i] == c:
                record[i] = 0
        count = 0
        while -1 in record:
            for j in range(len(record)):
                if record[j] == count:
                    if j-1 >= 0 :
                        record[j-1] = count + 1 if record[j-1] == -1 else record[j-1]
                    if j+1 < len(record):
                        record[j+1] = count + 1 if record[j+1] == -1 else record[j+1]
            count += 1
        return record