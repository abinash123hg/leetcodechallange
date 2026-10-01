class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        # Backtracking helper function
        def backtrack(current_path, remaining):
            if not remaining:
                result.append(list(current_path))
                return
            
            for i in range(len(remaining)):
                # Choose the element and recurse with the rest
                current_path.append(remaining[i])
                backtrack(current_path, remaining[:i] + remaining[i+1:])
                # Backtrack: remove the element to explore other possibilities
                current_path.pop()
                
        backtrack([], nums)
        return result