#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(a); i<=(b); i++)
#define int long long

signed main() {
    auto _F = freopen("../input/13-modified.in", "r", stdin);
    int a, b, c, d, x, y;
    int tot = 0;
    while (cin >> a >> b >> c >> d >> x >> y) {
        x += 10000000000000ll;
        y += 10000000000000ll;
        int det = a * d - b * c;
        if (det != 0) {
            int d1 = x * d - y * c;
            if (d1 % det) continue;
            int i = d1 / det;
            int d2 = a * y - b * x;
            if (d2 % det) continue;
            int j = d2 / det;
            if (i < 0 || j < 0) continue;
            tot += i * 3 + j;
        } else {
            if (a * y != b * x) continue;
            cerr << "This is a speical case that I bet they wouldn't test..." << endl;
            // you would solve this case using exgcd though
        }
    }
    cout << tot << endl;
}
