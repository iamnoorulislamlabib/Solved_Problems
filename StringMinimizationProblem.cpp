// https://codeforces.com/contest/1706/problem/A

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



void lithium_03(){
    LL n,m;cin>>n>>m;
    vector<LL>v(n);
    for(auto &i:v)cin>>i;
    string s(m,'B');
    for(auto &i:v){
        LL pos1 = i-1;
        LL pos2 = m-i;
        LL mn = min(pos1,pos2);
        LL mx = max(pos1,pos2);
        if(s[mn]=='A'){
            s[mx]='A';
        }else{
            s[mn]='A';
        }

    }
    cout<<s<<"\n";
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
