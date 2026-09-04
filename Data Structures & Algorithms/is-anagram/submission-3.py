class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        
        # check length
        if len(s) != len(t):
            return false
        
        # same length
        for char in s:
            count[ord(char) - 97] += 1
        
        for char in t:
            if count[ord(char) - 97] == 0:
                return false
            else:
                count[ord(char) - 97] -= 1
        
        return True
