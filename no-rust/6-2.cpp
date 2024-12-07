#include<bits/stdc++.h>
using namespace std;

#define For(i, n) for(int i=0; i<(n); i++)

string s;
vector<string> game;
int n, m;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

bool check(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

set<pair<int, int>> path;

void first_walk(int x, int y) {
    int dir = 0;
    while (1) {
        if (!check(x, y)) break;

        path.insert(make_pair(x, y));

        while (check(x + dx[dir], y + dy[dir]) && game[x + dx[dir]][y + dy[dir]] == '#') {
            dir++;
            dir %= 4;
        }

        x += dx[dir];
        y += dy[dir];
    }
}




set<tuple<int, int, int>> vis;
bool check_loop(int sx, int sy) {
    vis.clear();
    int dir = 0;
    int x = sx;
    int y = sy;
    while (1) {
        if (!check(x, y)) break;
        
        auto state = make_tuple(x, y, dir);
        if (vis.count(state)) {
            return true;
        }
        vis.insert(state);

        while (check(x + dx[dir], y + dy[dir]) && game[x + dx[dir]][y + dy[dir]] == '#') {
            dir++;
            dir %= 4;
        }

        x += dx[dir];
        y += dy[dir];
    }

    return false;
}

int main() {
    freopen("../input/6.in", "r", stdin);
    while (cin >> s) {
        game.push_back(s);
        m = s.length();
    }
    n = game.size();

    int x, y;
    For(i, n) {
        For(j, m) {
            if (game[i][j] == '^') {
                x = i;
                y = j;
                break;
            }
        }
    }

    first_walk(x, y);

    int ans = 0;
    for (auto [i, j] : path) {
            if (game[i][j] != '.') continue;
            game[i][j] = '#';
            if (check_loop(x, y)) ans++;
            game[i][j] = '.';
    }
    cout << ans << endl;
}