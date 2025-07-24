#O(logx base 10) which is the number of digits of x 
class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        i=0
        j=len(y)-1
        while i<j:
            if y[i]==y[j]:
                i+=1
                j-=1
            else:
                return False
        return True
