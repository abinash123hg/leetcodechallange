class Solution:
    def combinationSum(self, candidates, target):
        result = []

        candidates.sort()

        def backtrack(start, current_comb, current_sum):
            if current_sum == target:
                result.append(current_comb.copy())
                return

            for i in range(start, len(candidates)):
                value = candidates[i]

                if current_sum + value > target:
                    break

                current_comb.append(value)

                # Use i, not i + 1, because values may be reused
                backtrack(i, current_comb, current_sum + value)

                current_comb.pop()

        backtrack(0, [], 0)
        return result
        return result