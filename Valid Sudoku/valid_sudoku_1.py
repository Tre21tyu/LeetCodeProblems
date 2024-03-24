from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Dictionaries 
        rows = {} 
        cols = {} 
        three_by_three = {} 
        for i in range(len(board)):
            row_vals = []
            col_vals = []
            box_vals = []
            for j in range(len(board)):
                # Add to row dictionary
                row_cell = board[i][j]
                # Add to col dictionary
                col_cell = board[j][i]

                if row_cell != ".": row_vals.append(int(row_cell))
                if col_cell != ".": col_vals.append(int(col_cell))

            rows[i] = row_vals
            cols[i] = col_vals
            # Add to 3x3 dictionary
        return f"Rows: {rows},\n Cols: {cols}"

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
