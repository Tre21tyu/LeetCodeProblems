#include <iostream>
using namespace std;

int main() {
    bool row[9][9] = {false};
    bool col[9][9] = {false};

    // Assume we have a sudoku grid represented by a 9x9 2D array
    int sudokuGrid[9][9] = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}
    };

    // Update the boolean arrays based on the given sudoku grid
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            int num = sudokuGrid[i][j];
            if (num != 0) {
                row[i][num - 1] = true;
                col[j][num - 1] = true;
            }
        }
    }

    // Printing the status of row and col arrays
    cout << "Row status:" << endl;
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            cout << row[i][j] << " ";
        }
        cout << endl;
    }

    cout << "\nColumn status:" << endl;
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            cout << col[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}

