class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])

        p_q = deque()
        p_seen = set()
        a_q = deque()
        a_seen = set()

        for i in range(n):
            p_q.append((0,i))
            p_seen.add((0,i))
        for i in range(1,m):
            p_q.append((i,0))
            p_seen.add((i,0))
        
        for i in range(m):
            a_q.append((i,n-1))
            a_seen.add((i,n-1))
        for i in range(n-1):
            a_q.append((m-1,i))
            a_seen.add((m-1,i))


        def getcord(q, seen):
            while q:
                i,j = q.popleft()
                seen.add((i,j))

                for i_of, j_of in [(0,1),(1,0),(-1,0),(0,-1)]:
                    r, c = i+i_of, j+j_of
                    if 0<=r<m and 0<=c<n and heights[r][c]>=heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        q.append((r,c))
            return seen
        
        p_cord = getcord(p_q, p_seen)
        a_cord = getcord(a_q, a_seen)

        return list(p_cord.intersection(a_cord))