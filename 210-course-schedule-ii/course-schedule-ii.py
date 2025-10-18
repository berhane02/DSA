class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        g = defaultdict(list)
        for a,b in prerequisites:
                g[a].append(b)
        notvisited, visiting, visited = 0,1,2

        status = [notvisited]*numCourses
        res = []
        def dfs(i):
            if status[i] == visiting: return False
            if status[i] == visited: return True

            status[i] = visiting

            for n in g[i]:
                if dfs(n) == False: return False
            status[i] = visited
            res.append(i)
            return True
        
        for i in range(numCourses):
            if dfs(i) is not True:
                return []
        return res