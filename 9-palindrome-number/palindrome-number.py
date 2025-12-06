class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        l1,l2 = 0, len(num)-1
        if num[l1] == "-":
            return False

        while l1<=l2:

            if num[l1] != num[l2]:
                return False
            l1+=1
            l2-=1
        return True