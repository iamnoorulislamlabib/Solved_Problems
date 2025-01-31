// https://codeforces.com/contest/2060/problem/C

/*
B&H
*/

#include <bits/stdc++.h>
using namespace std;

#define LL long long

#define faster \
{              \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);                   \
}

inline void debugMode() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

inline void runtime(clock_t tStart) {
#ifndef ONLINE_JUDGE
    fprintf(stderr, "\n>> Runtime: %.10fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
#endif
}

bool cmp(vector<LL>&a,vector<LL>&b){
    return a[1]<b[1];
}

void lithium_03(){
    LL n,m;cin>>n>>m;
    map<LL,LL>mp;
    vector<LL>v(n);
    for(auto &i:v)cin>>i;
    LL ans = 0;
    for(auto &i:v){
        LL dif = m-i;
        if(dif<0)continue;
        if(mp[dif]>0){
            ans++;
            mp[dif]--;
        }
        else{
            mp[i]++;
        }
    }
    cout<<ans<<"\n";
}

int main() {
    clock_t tStart = clock();
    faster;
    debugMode();

    LL testCases = 1;
    cin >> testCases;

    for (LL i = 1; i <= testCases; i++) {
        lithium_03();
    }

    runtime(tStart);
    return 0;
}

