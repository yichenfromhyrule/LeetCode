class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap1 = {}
        hashmap2 = {}
        copy1 = ""
        copy2 = ""
        if len(s)!=len(t):
            return False
        else:
            start1 = 0
            start2 = 0
            for i in range(0, len(s)):
                if s[i] not in hashmap1:
                    start1 += 1
                    hashmap1[s[i]] = start1
                    copy1 += str(start1)
                else:
                    copy1 += str(hashmap1[s[i]])

                if t[i] not in hashmap2:
                    start2 += 1
                    hashmap2[t[i]] = start2
                    copy2 += str(start2)
                else:
                    copy2 += str(hashmap2[t[i]])

        print(copy1, copy2)
        return  copy2 == copy1

if __name__ == '__main__':
    s = Solution()
    s1 = "foo"
    s2 = "bar"
    r = s.isIsomorphic(s1,s2)
    print(r)