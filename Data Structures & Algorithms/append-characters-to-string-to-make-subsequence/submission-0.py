class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p1 = 0
        p2 = 0
        len_t, len_s = len(t),len(s)
        while p1<len_s and p2<len_t:
            if s[p1]==t[p2]:
                p2+=1
            p1+=1

        return len_t- p2
    