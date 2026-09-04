class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for i in range(0, len(strs)):
            anagrams_for_word_i = []
            
            # if word has been considered
            if strs[i] in anagrams:
                continue

            for j in range(i+1, len(strs)):
                if len(strs[i]) == len(strs[j]):
                    # check for anagram
                    word_a = strs[i]
                    word_b = strs[j]
                    
                    is_anagram = False
                    
                    # split the word_a and split word_b
                    list_word_a = list(word_a)
                    list_word_b = list(word_b)

                    for char in list_word_a:
                        if char not in list_word_b:
                            is_anagram = False
                            break
                        else:
                            list_word_b.pop(list_word_b.index(char))
                    
                    if len(list_word_b) == 0:
                        is_anagram = True
                    
                    if is_anagram:
                        anagrams_for_word_i.append(strs[j])
            anagrams_for_word_i.append(strs[i])
            anagrams.append(anagrams_for_word_i)
            
        return anagrams
