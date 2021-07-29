class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        hashmap = {}
        for j in range(len(s) - 1, -1, -1):
            if s[j] not in hashmap:
                hashmap[s[j]] = j

        index_list = []
        for c in s:
            index_list.append(hashmap[c])

        result = [-1]
        start_index = 0
        while start_index < len(index_list):
            end_target = index_list[start_index]
            while start_index != end_target:
                start_index += 1
                end_target = max(end_target, index_list[start_index])
            result.append(end_target)
            start_index += 1
        return [result[m] - result[m - 1] for m in range(1, len(result))]


