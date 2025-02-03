// https://codeforces.com/problemset/problem/2043/B

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
    LL n,d;cin>>n>>d;
    vector<LL>ans(10,0);
    ans[1]=1;
    if(d==7)ans[d]=1;
    if(n>=3)ans[7]=1;
    if(n>=3)ans[3]=1;
    if(d==3 || d==6 || d==9)ans[3]=1;
    if(d==5)ans[d]=1;
    if(d==9)ans[d]=1;
    if(d==3 || d==6){
        if(n>=3)ans[9]=1;
    }
    if(n>=6)ans[9]=1;

    for(LL i=1;i<=9;i++){
        if(ans[i])cout<<i<<" ";
    }
    cout<<"\n";

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
