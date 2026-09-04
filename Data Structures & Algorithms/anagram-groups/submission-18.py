class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_groups = {}

        for word in strs:
            count = [0] * 26
            
            for character in word:
                count[ord(character) - 97] += 1
            word_groups[tuple(count)].append(word)
        
        return list(word_groups.values())