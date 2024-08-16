#include <iostream>
#include <bits/stdc++.h>
#include <ctime>
using namespace std;

void calculateElapsedTime(struct timespec &start, struct timespec &end) {
    long seconds = end.tv_sec - start.tv_sec;
    long nanoseconds = end.tv_nsec - start.tv_nsec;
    double elapsed = seconds + nanoseconds * 1e-9;
    std::cout << "Elapsed time: " << elapsed << " seconds" << std::endl;
}

long long fibonacci_loop_memoization(int n) {
    vector<long long> memo(n + 1, -1);

    memo[0] = 0;
    memo[1] = 1;

    for (int i = 2; i <= n; ++i) {
        memo[i] = memo[i - 1] + memo[i - 2];
    }

    return memo[n];
}

int main(){
    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC,&start);
    
    int n = 50;
    for(int i=0; i<n; i++){
        cout<<fibonacci_loop_memoization(i)<<" ";
    }
    cout<<endl;
    clock_gettime(CLOCK_MONOTONIC, &end);
    calculateElapsedTime(start, end);

    return 0;

}