#include <iostream>
#include <vector>
#include <sstream>

void marshalCoaches() {
    while (true) {
        int trainLength;
        std::cin >> trainLength;

        if (trainLength == 0) {
            break;
        }

        while (true) {
            std::string permutation;
            std::cin >> permutation;

            if (permutation == "0") {
                break;
            }

            std::istringstream iss(permutation);
            std::vector<int> coachPermutation;

            int listItem;
            while (iss >> listItem) {
                coachPermutation.push_back(listItem);
            }

            std::vector<int> stationStack;
            int expectedCoach = 1;

            for (int coach : coachPermutation) {
                while (!stationStack.empty() && stationStack.back() == expectedCoach) {
                    stationStack.pop_back();
                    expectedCoach++;
                }

                if (coach == expectedCoach) {
                    expectedCoach++;
                } else {
                    stationStack.push_back(coach);
                }
            }

            if (stationStack.empty()) {
                std::cout << "Yes" << std::endl;
            } else {
                std::cout << "No" << std::endl;
            }
        }

        std::cout << std::endl;
    }
}

int main() {
    marshalCoaches();
    return 0;
}