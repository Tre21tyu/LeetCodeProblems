#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

class Solution {
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        std::unordered_map<int, std::unordered_set<char>> cols;
        std::unordered_map<int, std::unordered_set<char>> rows;
        std::unordered_map<int, std::unordered_set<char>> sqrs;  // key = (r /3, c /3)

        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                char cell = board[r][c];
                if (cell == '.')
                    continue;
                if (rows[r].count(cell) > 0 || cols[c].count(cell) > 0 || sqrs[(r / 3) * 3 + c / 3].count(cell) > 0)
                    return false;
                cols[c].insert(cell);
                rows[r].insert(cell);
                sqrs[(r / 3) * 3 + c / 3].insert(cell);
            }
        }
        return true;
    }
};

int main() {
    Solution solution;
    std::vector<std::vector<char>> testcase = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
    };

    std::cout << std::boolalpha << solution.isValidSudoku(testcase) << std::endl;
    return 0;
}
