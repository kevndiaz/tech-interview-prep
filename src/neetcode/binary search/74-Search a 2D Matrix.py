from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target and matrix[m][len(matrix[m]) - 1] >= target:
                hold = m
                l, r = 0, len(matrix[hold]) - 1

                while l <= r:
                    m = (l + r) // 2

                    if matrix[hold][m] == target:
                        return True
                    elif matrix[hold][m] < target:
                        l = m + 1
                    else:
                        r = m - 1

                return False
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        return False