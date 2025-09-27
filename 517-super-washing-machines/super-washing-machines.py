class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        sumM = sum(machines)
        
        if sumM % len(machines) != 0:
            return -1
        
        res = 0
        avg = sumM // len(machines)
        running_machine = 0

        for n in machines:
            num_mov = n - avg
            running_machine += num_mov
            res = max(res, abs(running_machine), num_mov)
        return res
        