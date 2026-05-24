class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                count[index] += 1
            seen[tuple(count)].append(word)
        return list(seen.values())