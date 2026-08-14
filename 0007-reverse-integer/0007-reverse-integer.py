class Solution:

  def reverse(self, x: int) -> int:
    # Set 32-bit integer limits
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    # Handle the sign
    sign = -1 if x < 0 else 1
    res = int(str(abs(x))[::-1]) * sign

    # Check for overflow
    if res < INT_MIN or res > INT_MAX:
      return 0

    return res