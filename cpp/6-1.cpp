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

    int dir = 0;
    while (1) {
        if (!check(x, y)) break;

        game[x][y] = 'X';

        while (check(x + dx[dir], y + dy[dir]) && game[x + dx[dir]][y + dy[dir]] == '#') {
            dir++;
            dir %= 4;
        }

        x += dx[dir];
        y += dy[dir];
    }
    int ans = 0;
    For(i, n) {
        For(j, m) {
            if (game[i][j] == 'X') ans++;
        }
    }
    cout << ans << endl;
}