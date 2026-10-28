class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i, val in enumerate(nums):
            # If our current index is beyond the maximum reach we can achieve, we're stuck
            if i > max_reach:
                return False
            
            # Update the furthest index we can reach from here
            max_reach = max(max_reach, i + val)
            
            # If max_reach can already cover or exceed the last index, return True early
            if max_reach >= len(nums) - 1:
                return True
                
        return True