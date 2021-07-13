class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap1 = {}
        hashmap2 = {}
        if len(s)!=len(t):
            return False
        else:
            for i in range(0, len(s)):
                if s[i] not in hashmap1:
                    hashmap1[s[i]] = [i]
                else:
                    hashmap1[s[i]].append(i)
                if t[i] not in hashmap2:
                    hashmap2[t[i]] = [i]
                else:
                    hashmap2[t[i]].append(i)
        print(hashmap1, hashmap2)
        l1 = list(hashmap1.values())
        l2 = list(hashmap2.values())
        print(l1, l2)
        return  l1==l2

if __name__ == '__main__':
    s = Solution()
    s1 = "foo"
    s2 = "bar"
    r = s.isIsomorphic(s1,s2)
    print(r)