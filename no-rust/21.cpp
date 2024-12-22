#include <bits/stdc++.h>
using namespace std;

struct Pos
{
    int i;
    int j;
    bool operator<(const Pos &other) const
    {
        return tie(i, j) < tie(other.i, other.j);
    }
    Pos operator+(const Pos &other) const
    {
        return Pos{i + other.i, j + other.j};
    }
    Pos operator-(const Pos &other) const
    {
        return Pos{i - other.i, j - other.j};
    }
    bool operator==(const Pos &other) const
    {
        return i == other.i && j == other.j;
    }
};

struct Key
{
    int robot_id;
    char current_key;
    char dest_key;
    int total_robots;
    bool operator<(const Key &other) const
    {
        return tie(robot_id, current_key, dest_key, total_robots) < tie(other.robot_id, other.current_key, other.dest_key, other.total_robots);
    }
};

vector<string> codes;
map<char, Pos> numpad = {
    {'7', Pos{0, 0}}, {'8', Pos{0, 1}}, {'9', Pos{0, 2}}, 
    {'4', Pos{1, 0}}, {'5', Pos{1, 1}}, {'6', Pos{1, 2}}, 
    {'1', Pos{2, 0}}, {'2', Pos{2, 1}}, {'3', Pos{2, 2}}, 
    {'0', Pos{3, 1}}, {'A', Pos{3, 2}}};
map<Pos, char> numpad_inv;
map<char, Pos> dirpad = {
    {'^', Pos{0, 1}}, {'A', Pos{0, 2}}, 
    {'<', Pos{1, 0}}, {'v', Pos{1, 1}}, {'>', Pos{1, 2}}};
map<Pos, char> dirpad_inv;
map<char, Pos> dirs = {
    {'^', Pos{-1, 0}}, {'v', Pos{1, 0}}, 
    {'<', Pos{0, -1}}, {'>', Pos{0, 1}}};
unordered_map<long long, long long> memo;

long long func(int robot_id, char current_key, char dest_key, int total_robots)
{
    Key k = Key{robot_id, current_key, dest_key, total_robots};
    long long key_hash = ((long long)robot_id << 40) | ((long long)current_key << 32) | ((long long)dest_key << 16) | total_robots;
    if (memo.find(key_hash) != memo.end())
        return memo[key_hash];
    map<char, Pos> pad;
    map<Pos, char> pad_inv_map;
    if (robot_id == 0)
    {
        pad = numpad;
        pad_inv_map = numpad_inv;
    }
    else
    {
        pad = dirpad;
        pad_inv_map = dirpad_inv;
    }
    Pos current_pos = pad[current_key];
    Pos dest_pos = pad[dest_key];
    Pos delta = dest_pos - current_pos;
    if (robot_id == total_robots - 1)
    {
        memo[key_hash] = abs(delta.i) + abs(delta.j) + 1;
        return memo[key_hash];
    }
    vector<char> seq;
    if (delta.i < 0)
    {
        for (int x = 0; x < abs(delta.i); x++)
            seq.push_back('^');
    }
    else
    {
        for (int x = 0; x < abs(delta.i); x++)
            seq.push_back('v');
    }
    if (delta.j < 0)
    {
        for (int x = 0; x < abs(delta.j); x++)
            seq.push_back('<');
    }
    else
    {
        for (int x = 0; x < abs(delta.j); x++)
            seq.push_back('>');
    }
    if (seq.empty())
    {
        memo[key_hash] = 1;
        return 1;
    }
    set<vector<char>> perms;
    sort(seq.begin(), seq.end());
    do
    {
        perms.emplace(seq);
    } while (next_permutation(seq.begin(), seq.end()));
    long long min_steps = LLONG_MAX;
    for (auto &r : perms)
    {
        Pos pos = current_pos;
        long long steps = 0;
        bool valid = true;
        for (int i = 0; i < r.size(); i++)
        {
            char dir_key = r[i];
            char prev_key = i == 0 ? 'A' : r[i - 1];
            steps += func(robot_id + 1, prev_key, dir_key, total_robots);
            pos = pos + dirs[dir_key];
            if (pad_inv_map.find(pos) == pad_inv_map.end())
            {
                valid = false;
                break;
            }
        }
        if (valid)
        {
            char last_dir = r.back();
            steps += func(robot_id + 1, last_dir, 'A', total_robots);
            min_steps = min(min_steps, steps);
        }
    }
    memo[key_hash] = min_steps;
    return min_steps;
}

int main()
{
    for (auto &[k, v] : numpad)
        numpad_inv[v] = k;
    for (auto &[k, v] : dirpad)
        dirpad_inv[v] = k;
    ifstream infile("../input/21.in");
    string line;
    while (getline(infile, line))
    {
        if (!line.empty())
            codes.push_back(line);
    }
    long long total_complexity;
    for (int num_robots : {3, 26})
    {
        total_complexity = 0;
        for (auto &code : codes)
        {
            long long complexity = func(0, 'A', code[0], num_robots);
            for (int i = 1; i < code.size(); i++)
                complexity += func(0, code[i - 1], code[i], num_robots);
            string num_str = code.substr(0, code.size() - 1);
            long long num = stoll(num_str);
            total_complexity += complexity * num;
        }
        cout << total_complexity << "\n";
    }
}
