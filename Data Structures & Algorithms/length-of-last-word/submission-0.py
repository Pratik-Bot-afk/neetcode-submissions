class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        for i in range(-1,-len(s) - 1, -1):
            if s[i].isspace():
                if count > 0: break
                continue 
            elif s[i].isalpha():
                count=count+1
        return count