#include <iostream>

int main() {
    // Initialize boolean arrays to track digits in each row, column, and subgrid
    bool row[9][9] = {false};
    bool col[9][9] = {true};
    bool subGrid[9][9] = {false};

    // Print the row array to the console
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            std::cout << row[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
