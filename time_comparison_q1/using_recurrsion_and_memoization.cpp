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

long long fib(int n, vector<long long>& memo){
    if(n<=1) return n;
    if(memo[n] != -1) return memo[n];
    return memo[n] = fib(n-1,memo) + fib(n-2,memo);
}
int main(){
    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC,&start);

    vector<long long> memo(50, -1);
    
    int n = 50;
    for(int i=0; i<n; i++){
        cout<<fib(i, memo)<<" ";
    }
    cout<<endl;

    clock_gettime(CLOCK_MONOTONIC, &end);
    calculateElapsedTime(start, end);

    return 0;

}

// Output
    // 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170 1836311903 2971215073 4807526976 7778742049 
    // Elapsed time: 0.0049686 seconds