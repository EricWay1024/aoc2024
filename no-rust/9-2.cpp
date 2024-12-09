#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

pair<int, int> get_range(const vector<int>& m, int i) {
    int a = i, b = i;
    while (a >= 1 && m[a - 1] == m[i]) {
        a--;
    }
    while (b + 1 < m.size() && m[b + 1] == m[i]) {
        b++;
    }
    return {a, b};
}

vector<int> m;
int main() {
    freopen("../input/9.in", "r", stdin);
    string f; 
    cin >> f; 
    // string f = "2333133121414131402";
    
    int id_num = 0;

    for (int i = 0; i < f.size(); ++i) {
        int k = f[i] - '0';
        for (int j = 0; j < k; ++j) {
            if (i % 2 == 1) {
                m.push_back(-1);
            } else {
                m.push_back(id_num);
            }
        }
        if (i % 2 == 1) {
            id_num++;
        }
    }

    int j = m.size() - 1;

    while (j >= 0) {
        auto [a, b] = get_range(m, j);
        int len_j = b - a + 1;

        int i = 0;
        while (i < j) {
            if (m[i] != -1) {
                i++;
                continue;
            }

            auto [c, d] = get_range(m, i);
            int len_i = d - c + 1;

            if (len_i >= len_j) {
                for (int k = 0; k < len_j; ++k) {
                    swap(m[c + k], m[a + k]);
                }
                break;
            } else {
                i = d + 1;
            }
        }
        j--;
        // if (j % 100 == 0) cout << j << "\n";
    }
    long long ans = 0;
    for (int i = 0; i < m.size(); ++i) {
        if (m[i] != -1) {
            ans += i * m[i];
        }
    }
    cout << ans << endl;
    return 0;
}
