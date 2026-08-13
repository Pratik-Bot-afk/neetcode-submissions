class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        while p1<len(s):
            if p2>=len(t):
                return False
            elif  t[p2] == s[p1]:
                p1+=1
                p2+=1
            else :
                p2+=1
        return True

            

            