#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;
#define ll long long

void fast_do(long long a) {
    long long b = 0;
    while (a) {
        b = a & 7ll;
        b ^= 3ll;
        b ^= (a >> b);
        b ^= 5ll;
        cout << (b & 7ll) << ",";
        a /= 8ll;
    }
    cout << endl;
}

int do_part(long long a) {
    long long b = (a & 7ll);
    b ^= 3ll;
    b ^= (a >> b);
    b ^= 5ll;
    return (b & 7ll);
}

std::vector<int> program = {2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0};

void dfs(long long a, int cur) {
    if (cur == -1) {
        cout << a << endl;
        return;
    }

    long long o = program[cur];

    for (int i = 0; i < 8; i++) {
        ll new_a = (a << 3) | i;
        if (do_part(new_a) == o) {
            dfs(new_a, cur - 1);
        }
    }
}

int main() {
    // fast_do(45483412ll);
    // exit(0);

    dfs(0, program.size() - 1);

    return 0;
}
