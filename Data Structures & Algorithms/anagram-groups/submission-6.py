class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hashmap to save and use the characters as the keys
        grouping = {}
        for s in strs:
            numChar = [0] * 26
            for char in s:
                index = ord(char) - ord("a")
                numChar[index] += 1
            numChar = tuple(numChar)
            if numChar in grouping:
                grouping[numChar].append(s)
            else:
                grouping[numChar] = [s]
        return list(grouping.values())  