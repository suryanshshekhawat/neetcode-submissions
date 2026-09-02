class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        
        # check length
        if len(s) != len(t):
            return False
        
        # same length
        for char in s:
            count[ord(char) - 97] += 1
        
        for char in t:
            if count[ord(char) - 97] == 0:
                return False
            else:
                count[ord(char) - 97] -= 1
        
        return True
