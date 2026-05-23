class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countings = {}
        countingt = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in countings:
                countings[s[i]] += 1
            else:
                countings[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in countingt:
                countingt[t[i]] += 1
            else:
                countingt[t[i]] = 1

        for i in countings:
            if countings[i] != countingt.get(i, 0):
                return False
        return True