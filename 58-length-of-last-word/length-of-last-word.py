class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces, then split the string into words by whitespace
        words = s.split()
        
        # Return the length of the last word in the list
        return len(words[-1]) if words else 0