class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        n=len(num)-1
        l= len(num)//2
        
        for i in range(0, l):
            if num[i]!=num[n-i]:
                return False
        return True