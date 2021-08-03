class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        init_item = "(" * n + ")"
        init_list = [init_item]
        need_right = n - 1  # need n-1 ")"
        while need_right > 0:
            new_list = []
            for curr_str in init_list:
                check_left = n - need_right
                i = 0
                count_left = 0
                while count_left < check_left:
                    if curr_str[i] == "(":
                        count_left += 1
                    if count_left == check_left:
                        new_str = curr_str[:i + 1] + ")" + curr_str[i + 1:]
                        new_list.append(new_str)
                        if check_left < n:
                            check_left += 1
                    i += 1
            init_list = list(set(new_list))
            need_right -= 1

        return init_list
