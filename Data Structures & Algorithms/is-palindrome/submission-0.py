class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip().lower()
        l=0
        r=len(s)-1
        while l<r :
            if not s[l].isalnum():
                l=l+1
            elif not s[r].isalnum():
                r=r-1
            elif s[l]!=s[r]:
                return False
            else:
                l=l+1
                r=r-1
        return True

