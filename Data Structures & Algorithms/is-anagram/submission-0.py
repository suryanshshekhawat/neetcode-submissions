class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_2 = list(s)
        s_2.sort()
        t_2 = list(t)
        t_2.sort()
        return "".join(s_2) == "".join(t_2)