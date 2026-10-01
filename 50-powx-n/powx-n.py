class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Helper function for recursive binary exponentiation
        def helper(base, exp):
            if exp == 0:
                return 1.0
            if base == 0:
                return 0.0
            
            res = helper(base * base, exp // 2)
            return res * base if exp % 2 != 0 else res

        if n < 0:
            return 1.0 / helper(x, -n)
        return helper(x, n)