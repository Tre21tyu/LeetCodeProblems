import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                if (
                        cell in rows[r]
                        or cell in cols[c]
                        or cell in sqrs[(r // 3, c // 3)]
                        ):
                    return False
                cols[c].add(cell)
                rows[r].add(cell)
                sqrs[(r // 3, c // 3)].add(cell)

        return True
solution = Solution()
testcase = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSudoku(testcase))
