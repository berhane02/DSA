class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        return num == num[::-1]
        # n=len(num)
        
        # for i in range(0, n//2):
        #     if num[i]!=num[n-1-i]:
        #         return False
        # return True