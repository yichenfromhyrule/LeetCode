class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        return sum(salary[1:-1])/float(len(salary)-2)