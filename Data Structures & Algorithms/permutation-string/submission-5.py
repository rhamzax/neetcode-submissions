class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = [0] * 26
        for char in s1:
            count[ord(char)-ord('a')] += 1
        

        check = [0] * 26
        windowMax = len(s1)
        for char in range(windowMax):
            check[ord(s2[char])-ord('a')] += 1
        
        for r in range(windowMax, len(s2)):
            if check == count:
                return True
            else:
                oldChar = s2[r-windowMax]
                check[ord(oldChar)-ord('a')] -= 1
                currentChar = s2[r]
                check[ord(currentChar)-ord('a')] += 1
                print(check, count)
        if check == count:
            return True
        return False
            