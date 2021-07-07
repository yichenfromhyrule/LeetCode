class Solution(object):
    def findPalindrome(self, s, left_key, right_key, current_result, all_same, same_character):
        if left_key>=0 and right_key<len(s):
            if s[left_key]==s[right_key]:
                current_result = s[left_key:right_key+1]
                if all_same and s[left_key]!=same_character:
                    all_same=False
                left_key -= 1
                right_key += 1
                #print(left_key, right_key, current_result, all_same, same_character)
                return self.findPalindrome(s, left_key, right_key, current_result, all_same, same_character)
            else:
                if all_same and (s[left_key]==same_character or s[right_key]==same_character):
                    if s[left_key]==same_character:
                        current_result = s[left_key]+current_result
                        left_key -= 1
                    else:
                        current_result = current_result+s[right_key]
                        right_key += 1
                    #print(left_key, right_key,current_result,all_same,same_character)
                    return self.findPalindrome(s, left_key, right_key, current_result, all_same, same_character)
                else:
                    return current_result
        else:
            if (left_key>=0 or right_key<len(s)) and all_same:
                if left_key>=0:
                    if s[left_key]==same_character:
                        current_result = s[left_key] + current_result
                        left_key -= 1
                        return self.findPalindrome(s, left_key, right_key, current_result, all_same, same_character)
                    else:
                        return current_result
                else:
                    if s[right_key]==same_character:
                        current_result += s[right_key]
                        right_key += 1
                        return self.findPalindrome(s, left_key, right_key, current_result, all_same, same_character)
                    else:
                        return current_result
            else:
                return current_result

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(0, len(s)):
            current_result = s[i]
            all_same = True
            same_character = s[i]
            current_result = self.findPalindrome(s, i-1, i+1, current_result, all_same, same_character)
            print(s[i],i,current_result)
            if current_result:
                if len(result)<len(current_result):
                    result = current_result
                    if len(result)==len(s):
                        return result
        return result




if __name__ == '__main__':
    s = Solution()
    str = "ababababababa"
    r = s.longestPalindrome(str)
    print(r)