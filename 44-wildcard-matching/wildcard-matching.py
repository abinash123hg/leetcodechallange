class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx, p_idx = 0, 0
        star_idx = -1
        match = 0
        
        while s_idx < len(s):
            # If characters match or pattern has '?'
            if p_idx < len(p) and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            # If pattern has '*', mark the star position and current string index
            elif p_idx < len(p) and p[p_idx] == '*':
                star_idx = p_idx
                match = s_idx
                p_idx += 1
            # If we had a previous '*', we can backtrack and match more characters with '*'
            elif star_idx != -1:
                p_idx = star_idx + 1
                match += 1
                s_idx = match
            else:
                return False
            
        # Check remaining characters in pattern are all '*'
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == len(p)