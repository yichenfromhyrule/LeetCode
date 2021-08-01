class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                hashmap[pattern[i]].append(i)
            else:
                hashmap[pattern[i]] = [i]

        s_array = s.split(' ')
        if len(s_array) != len(pattern):
            return False
        checked = []
        for key in hashmap:
            l = [s_array[j] for j in hashmap[key]]
            if l[0] in checked or len(set(l)) != 1:
                return False
            checked.append(s_array[hashmap[key][0]])

        return True