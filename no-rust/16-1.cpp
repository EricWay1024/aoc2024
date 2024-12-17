#include <bits/stdc++.h>
using namespace std;
vector<string> grid;
#define For(i, n) for(int i=0; i<(n); i++)
#define ll long long
const vector<pair<int, int>> moves = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
ll dis[1000][1000][10];
bool vis[1000][1000][10];
#define State tuple<long long, int, int, int>
priority_queue<State> q;

ll best_ans = -1;
int n, m;
int str, stc, edr, edc;


void solve() {
    memset(dis, 0x3f, sizeof(dis));

    dis[str][stc][1] = 0;
    q.emplace(0, str, stc, 1);

    while (!q.empty()) {
        auto [cost, r, c, d] = q.top();
        cost = -cost;
        q.pop();
        if (vis[r][c][d]) {
            continue;
        }
        vis[r][c][d] = 1;

        vector<State> nss;
        for (int turn : { -1, 1 }) {
            int nd = (d + turn + 4) % 4;
            nss.emplace_back(cost + 1000, r, c, nd);
        }

        int dr = moves[d].first;
        int dc = moves[d].second;
        int nr = r + dr;
        int nc = c + dc;

        if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#') {
            nss.emplace_back(cost + 1, nr, nc, d);
        }

        for (auto &ns: nss) {
            auto [ncost, nr, nc, nd] = ns;
            if (dis[nr][nc][nd] > ncost) {
                dis[nr][nc][nd] = ncost;
                q.emplace(-ncost, nr, nc, nd);
            } 
        }
    }
}


int main() {
    freopen("../input/16.in", "r", stdin);
    string l;
    while (getline(cin, l)) {
        grid.push_back(l);
    }
    n = grid.size();
    m = grid[0].size();

    For(r, n) {
        For(c, m) {
            if (grid[r][c] == 'S') {
                str = r, stc = c;
            }
            if (grid[r][c] == 'E') {
                edr = r, edc = c;
            }
        }
    }

    solve();

    ll ans = INT32_MAX;
    For (i, 4) {
        ans = min(ans, dis[edr][edc][i]);
    }

    cout << ans << endl;
    
}