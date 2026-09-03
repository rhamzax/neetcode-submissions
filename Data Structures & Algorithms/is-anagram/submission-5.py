class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seenS = {}
        seenT = {}
        for i in range(len(s)):
            charseen = s[i]
            charseenT = t[i]
            if charseen not in seenS:
                seenS[charseen] = 1
            else:
                seenS[charseen] += 1
            if charseenT not in seenT:
                seenT[charseenT] = 1
            else:
                seenT[charseenT] += 1
        return seenS == seenT