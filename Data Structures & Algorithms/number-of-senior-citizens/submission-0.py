class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            age= details[i][-4]+details[i][-3]
            age=int(age)
            if age>60:
                count+=1
        return count 