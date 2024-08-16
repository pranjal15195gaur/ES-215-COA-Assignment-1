#include <iostream>
#include <ctime>
#include <vector>

using namespace std;

void matrixMultiply(int N, const vector<vector<int>> &matrix1, const vector<vector<int>> &matrix2, vector<vector<int>> &result) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            result[i][j] = 0;
            for (int k = 0; k < N; ++k) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
}


double calculateElapsedTime(struct timespec &start, struct timespec &end) {
    long seconds = end.tv_sec - start.tv_sec;
    long nanoseconds = end.tv_nsec - start.tv_nsec;
    return seconds + nanoseconds * 1e-9;
}

int main() {
    struct timespec cpustart,cpuend;
    clock_gettime(CLOCK_MONOTONIC, &cpustart);

    int N = 1024;
    vector<vector<int>> matrix1(N, vector<int>(N, 1));
    vector<vector<int>> matrix2(N, vector<int>(N, 2));
    vector<vector<int>> result(N, vector<int>(N, 0));

    struct timespec meatstart, meatend;
    clock_gettime(CLOCK_MONOTONIC, &meatstart);

    matrixMultiply(N, matrix1, matrix2, result);

    clock_gettime(CLOCK_MONOTONIC, &meatend);

    double MeatTime = calculateElapsedTime(meatstart, meatend);
    cout << "Matrix size: " << N << "x" << N << " | Meat time (Integer): " << MeatTime << " seconds" << endl;

    clock_gettime(CLOCK_MONOTONIC, &cpuend);

    double cpuTime = calculateElapsedTime(cpustart, cpuend);
    cout << "Matrix size: " << N << "x" << N << " | Elapsed time (Integer): " << cpuTime << " seconds" << endl;
    return 0;
}
