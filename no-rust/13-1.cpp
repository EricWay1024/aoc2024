#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(a); i<=(b); i++)

int main() {
    auto _F = freopen("../input/13-modified.in", "r", stdin);
    int a, b, c, d, x, y;
    int tot = 0;
    while (cin >> a >> b >> c >> d >> x >> y) {
        int ans = INT32_MAX;
        rep(i, 0, 100) {
            rep(j, 0, 100) {
                if (i * a + j * c == x && i * b + j * d == y) {
                    ans = min(ans, i * 3 + j);
                }
            }
        }
        if (ans != INT32_MAX) {
            tot += ans;
        }
    }
    cout << tot << endl;
}
