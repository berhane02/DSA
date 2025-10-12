class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]  # first element is always 1
        for i in range(1, rowIndex + 1):
            # compute next element using previous element
            row.append(row[i-1] * (rowIndex - i + 1) // i)
        return row
        