#include <iostream>
#include <vector>

using namespace std;

int calculate_moves() {
    int set_number = 1;

    while (true) {
        int columns;
        cin >> columns;

        if (columns == 0) {
            break;
        }

        vector<int> heights(columns);
        int total_bricks = 0;

        for (int i = 0; i < columns; ++i) {
            cin >> heights[i];
            total_bricks += heights[i];
        }

        int average_height = total_bricks / columns;
        int bricks_to_move = 0;

        for (int i = 0; i < columns; ++i) {
            if (heights[i] > average_height) {
                bricks_to_move += heights[i] - average_height;
            }
        }

        cout << "Set #" << set_number << endl;
        cout << "The minimum number of moves is " << bricks_to_move << ".\n\n";

        set_number++;
    }

    return 0;
}

int main() {
    calculate_moves();
    return 0;
}