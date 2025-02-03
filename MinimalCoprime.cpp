// https://codeforces.com/contest/2063/problem/A

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
    LL l,r;cin>>l>>r;
    LL ans = 0;
    if(l==r && l!=1){
        cout<<"0\n";
        return;
    }
    if(l==r && l==1){
        cout<<"1\n";
        return;
    }

    if(l==1){
        ans++;
        l++;
    }
    ans += (r-l);
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
