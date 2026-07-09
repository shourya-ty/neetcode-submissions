class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        mem_s = {}
        mem_t = {}
        for i in range(len(s)):
            mem_s[s[i]] = mem_s.get(s[i], 0) + 1
            mem_t[t[i]] = mem_t.get(t[i], 0) + 1
        
        for i in mem_s:
            try:
                mem_s[i]
                mem_t[i]
            except KeyError:
                return False
            if mem_s[i] != mem_t[i]:
                return False
        return True

            
