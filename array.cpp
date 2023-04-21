#include <iostream>
#include <ctime>

using namespace std;

const int SIZE = 1000000;
int arr[SIZE];

int main() {
    for (int i = 0; i<SIZE; i++) {
        arr[i] = i;
    }

    clock_t start, end;

    start = clock();
    for (int i = 0; i<100; i++) {
        for (int j = 0; j < SIZE; j++) {
            arr[j] += i;
        }
    }
    end = clock();
    cout << (float) (end - start) / (float) (CLOCKS_PER_SEC);

    return 0;
}