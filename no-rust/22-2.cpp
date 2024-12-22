// Warning: this one is super slow
#include <bits/stdc++.h>
using namespace std;

#define int long long

typedef pair<int, int> pii;

// Function to generate prices for a given initial secret
vector<pii> get_prices(int initial, int n=2000){
    int s = initial;
    vector<pii> prices;
    int last_price = initial % 10;
    for(int i=0;i<n;i++){
        s = (s * 64) ^ s;
        s %= 16777216;
        s = s ^ (s / 32);
        s %= 16777216;
        s = (s * 2048) ^ s;
        s %= 16777216;
        
        int cur_price = s % 10;
        prices.emplace_back(make_pair(cur_price, cur_price - last_price));
        last_price = cur_price;
    }
    return prices;
}

// Function to get occurrence based on pattern
int get_occurence(const vector<pii>& prices, const vector<int>& pattern){
    int n = prices.size();
    for(int i=3;i<n;i++){
        bool match = true;
        for(int j=0;j<4;j++){
            if(prices[i-3+j].second != pattern[j]){
                match = false;
                break;
            }
        }
        if(match){
            return prices[i].first;
        }
    }
    return 0;
}

set<tuple<int, int, int, int>> possible_patterns;

signed main(){
    // Read initial secrets from file
    vector<int> initial_secrets;
    ifstream infile("../input/22.in");

    string line;
    while(getline(infile, line)){
        if(!line.empty()){
            initial_secrets.push_back(stoi(line));
        }
    }
    infile.close();
    
    // Generate prices for each secret
    vector< vector<pii> > all_prices;
    all_prices.reserve(initial_secrets.size());
    for(auto secret : initial_secrets){
        auto prices = get_prices(secret);
        all_prices.emplace_back(prices);
    }


    for (int a=0; a<=9; a++) {
        for (int b=0; b<=9; b++) {
            for (int c=0; c<=9; c++) {
                for (int d=0; d<=9; d++) {
                    for (int e=0; e<=9; e++) {
                        possible_patterns.insert({b-a, c-b, d-c, e-d});
                    }
                }
            }
        }
    }
    
    int res = 0;
    for (auto &[a, b, c, d]: possible_patterns) {
        int ans = 0;
        vector<int> pattern = {a, b, c, d};
        for(size_t i=0;i<initial_secrets.size();i++){
            ans += get_occurence(all_prices[i], pattern);
        }
        res = max(ans, res);
    }

    cout << res << endl;
}
