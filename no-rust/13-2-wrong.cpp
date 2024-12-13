// I thought for a long time how to solve this using the Extended Euclidean algorithm
// only to realise that this is a linear system...
// This file is for entertaining purpose only

#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(a); i<=(b); i++)
#define int long long

void dbg() {cerr << "\n";}
template<typename T, typename... A> void dbg(T a, A... x) {cerr << a << ' '; dbg(x...);}
#define logs(x...) {cerr << #x << " -> "; dbg(x);}


tuple<int, int, int> exgcd(int a, int b) {
    if (b == 0) {
        return {a, 1, 0};
    } else {
        auto [d, x, y] = exgcd(b, a % b);
        return {d, y, x - (a / b) * y};
    }
}

tuple<bool, int, int> solve(int a, int b, int m) {
    auto [d, x0, y0] = exgcd(a, b);
    if ((m % d) != 0) return {false, 0, 0};
    return {true, m / d * x0, m / d * y0};
}

int real_mod(int a, int b) {
    return ((a%b) + b) % b;
}

signed main() {
    // auto _F = freopen("../input/13.in", "r", stdin);
    auto _F = freopen("../input/test.in", "r", stdin);
    int a, b, c, d, x, y;
    int tot = 0;
    while (cin >> a >> b >> c >> d >> x >> y) {
        x += 10000000000000ll;
        y += 10000000000000ll;


        auto [d1, i1, j1] = exgcd(a, c);
        if ((x % d1) != 0) continue;

        auto [d2, i2, j2] = exgcd(b, d);
        if ((y % d2) != 0) continue;

        a /= d1;
        c /= d1;
        x /= d1;
        i1 *= x;
        j1 *= x;
        // // solution i = i1 + k1 * c, j = j1 - k1 * a

        b /= d2;
        d /= d2;
        y /= d2;
        i2 *= y;
        j2 *= y;
        // // solution i = i2 + k2 * d, j = j2 - k2 * b

        auto [flag, x0, y0] = solve(c, -d, i2 - i1);
        if (!flag) continue;
        // // then i = i1 + c * (x0 + d * n) for n in NN
        int i = real_mod(i1 + c * x0,  c * d);

        int k1 = (i - i1) / c;
        int k2 = (i - i2) / d;

        // int i = real_mod(i1, c); // smallest possible i
        // int k1 = (i - i1) / c;
        // int j = j1 - k1 * a;

        // int ans = LONG_LONG_MAX;
        // while (j >= 0) {
        //     if (i * a + j * c == x && i * b + j * d == y) {
        //         ans = min(ans, i * 3 + j);
        //         break;
        //     }
        //     j -= a;
        //     i += c;

        //     // logs(i, j, a, c)
        // }

        // if (ans != LONG_LONG_MAX) {
        //     tot += ans;
        // }
    }
    cout << tot << endl;
}
