from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # Loop through rows and columns
        for i in range(n):
            start_row, start_col = (i // 3) * 3, (i % 3) * 3

            row_no_dots = [x for x in board[i] if x != "."] 
            col_no_dots = [row[i] for row in board if row[i] != "."]  # Get column elements
            three_by_three = [board[start_row + k][start_col + l] for k in range(3) for l in range(3) if board[start_row + k][start_col + l] != "."]
            if len(row_no_dots) > len(set(row_no_dots)):
                return False
            elif len(col_no_dots) > len(set(col_no_dots)):
                return False
            elif len(three_by_three) > len(set(three_by_three)):  # Check for duplicates in 3x3 block
                return False
        
        return True

solution = Solution()

testcase_1 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","0"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(solution.isValidSudoku(testcase_1))

