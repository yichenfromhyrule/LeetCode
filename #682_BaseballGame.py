class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score = []
        for op in ops:
            if op == "C":
                score = score[:-1]
            elif op == "D":
                score.append(score[-1] * 2)
            elif op == "+":
                score.append(score[-1] + score[-2])
            else:
                score.append(int(op))
        return sum(score)