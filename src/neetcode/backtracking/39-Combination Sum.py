from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i, subset):
            if i >= len(candidates):
                return

            total = sum(subset)

            if total == target:
                result.append(subset.copy())
                return
            elif total > target:
                return

            subset.append(candidates[i])
            dfs(i, subset)
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, subset)
        return result