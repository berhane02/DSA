class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for cord in points:
            dist = cord[0]**2+cord[1]**2
            if len(heap)<k:
                heapq.heappush(heap,(-dist, cord))
            else:
                heapq.heappushpop(heap, (-dist, cord))
        return [x for dist, x, in heap]