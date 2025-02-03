// https://codeforces.com/problemset/problem/2030/C

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
    LL n;cin>>n;
    string s;cin>>s;
    if(s[0]=='1' || s[n-1]=='1'){
        cout<<"YES\n";
        return;
    }

    for(LL i=0;i<n-1;i++){
        if(s[i]=='1' && s[i+1]=='1'){
            cout<<"YES\n";
            return;
        }
    }
    cout<<"NO\n";
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

