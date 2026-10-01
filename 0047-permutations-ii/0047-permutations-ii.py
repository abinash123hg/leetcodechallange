class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()
        visited = [False] * len(nums)
        
        def backtrack(current_path):
            if len(current_path) == len(nums):
                results.append(list(current_path))
                return
            
            for i in range(len(nums)):
                # If the element is already visited, skip it
                if visited[i]:
                    continue
                
                # If this element is a duplicate of the previous one and the 
                # previous one was not used in this branch, skip it to avoid duplicates
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                current_path.append(nums[i])
                backtrack(current_path)
                current_path.pop()
                visited[i] = False
                
        backtrack([])
        return results