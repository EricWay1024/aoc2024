#include <bits/stdc++.h>
using namespace std;
map<pair<long long, int>, long long> memo;
long long dp(long long x, int n) {
    if (n == 0)  return 1; 
    pair<long long, int> key = {x, n};
    if (memo.find(key) != memo.end()) return memo[key];
    if (x == 0) return memo[key] = dp(1, n - 1);
    else if (to_string(x).length() % 2 == 0) {
        string str_x = to_string(x);
        int mid = str_x.length() / 2;
        long long a = stoll(str_x.substr(0, mid));
        long long b = stoll(str_x.substr(mid));
        return memo[key] = dp(a, n - 1) + dp(b, n - 1);
    }
    else return memo[key] = dp(x * 2024, n - 1);
}

int main() {
    auto _F = freopen("../input/11.in", "r", stdin);
    vector<long long> f;
    string s;
    while (cin >> s) {
        f.push_back(stoll(s));
    }
    long long sum = 0;
    for (long long x : f) {
        sum += dp(x, 75);
    }
    cout << sum << endl;
    return 0;
}
