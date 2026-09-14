class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h_len, n_len = len(haystack), len(needle)
        
        for i in range(h_len - n_len + 1):
            if haystack[i:i + n_len] == needle:
                return i
                
        return -1