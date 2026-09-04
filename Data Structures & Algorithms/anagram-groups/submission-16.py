class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_groups = []

        considered_words = [0] * len(strs)

        for i in range(0, len(strs)):

            if considered_words[i] == 1:
                continue

            curr_word = strs[i]

            anagrams = list()
            anagrams.append(curr_word)
            
            considered_words[i] += 1
            
            for j in range(i + 1, len(strs)):
            
                if self._isAnagram(curr_word, strs[j]):
                    anagrams.append(strs[j])
                    considered_words[j] += 1

            word_groups.append(anagrams)
        
        return word_groups

    def _isAnagram(self, word_a: str, word_b:str) -> bool:
        
        count = [0] * 26

        # check for length
        if len(word_a) != len(word_b):
            return False

        for character in word_a:
            count[ord(character) - 97] += 1
        
        for character in word_b:
            if count[ord(character) - 97] == 0:
                return False
            else:
                count[ord(character) - 97] -= 1
        
        return True