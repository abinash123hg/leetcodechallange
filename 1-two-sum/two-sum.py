class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the value and its corresponding index
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            # Check if the complement already exists in our dictionary
            if complement in num_map:
                return [num_map[complement], i]
            # Otherwise, add the current number and its index to the dictionary
            num_map[num] = i