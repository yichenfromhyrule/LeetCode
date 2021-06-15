class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        num_points = len(graph)
        # 1. check every point connected with 0
        for i in range(num_points):
            path = [0]
            for point in graph[0]:
                self.findPath(graph, point, path)
                result.append(path)
        print("Result: ", result)
    def findPath(self, graph, start, path):
        if graph[start]:
            path.append(start)
            for point in graph[start]:
                if point == len(graph)-1:
                    path.append(point)
                    print("Path is: ", path)
                else:
                    self.findPath(graph, point, path)




if __name__ == '__main__':
    s = Solution()
    g = [[4,3,1],[3,2,4],[3],[4],[]]
    #s.allPathsSourceTarget(g)
    a = "jhdsgdg"
    p = a.split('z')
    print(p)