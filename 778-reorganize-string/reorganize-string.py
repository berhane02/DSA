class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt, in count.items()]
        heapq.heapify(maxHeap)

        prev = [0,'']
        res = ""

        while maxHeap:
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev[0]<0:
                heapq.heappush(maxHeap, prev)
            prev = [cnt, char]
        return res if len(res) == len(s) else ""