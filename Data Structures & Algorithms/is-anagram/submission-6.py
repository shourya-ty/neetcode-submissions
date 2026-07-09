class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        mem_s = {}
        mem_t = {}
        
        # Count frequencies
        for i in range(len(s)):
            mem_s[s[i]] = mem_s.get(s[i], 0) + 1
            mem_t[t[i]] = mem_t.get(t[i], 0) + 1
        
        # In Python, you can compare two dicts directly!
        # It automatically checks if keys and values match perfectly.
        return mem_s == mem_t
