class Solution:

  def shortestPalindrome(self, s: str) -> str:
    if not s:
      return s

    rev_s = s[::-1]
    combined = s + '#' + rev_s
    n = len(combined)

    # Build KMP prefix table (LPS array)
    lps = [0] * n
    for i in range(1, n):
      j = lps[i - 1]
      while j > 0 and combined[i] != combined[j]:
        j = lps[j - 1]
      if combined[i] == combined[j]:
        j += 1
      lps[i] = j

    # Length of longest palindromic prefix
    palindrome_len = lps[-1]

    # Prepend the reverse of the remaining non-palindromic suffix
    return rev_s[: len(s) - palindrome_len] + s