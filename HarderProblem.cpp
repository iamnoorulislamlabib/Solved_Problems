// https://codeforces.com/contest/2044/problem/D

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
    vector<LL>v(n);
    for(auto &i:v)cin>>i;
    vector<bool>vis(n+1,false);
    vector<LL>ans(n);
    LL k=1;
    for(LL i=0;i<n;i++){
        if(vis[v[i]]==false){
            vis[v[i]]=true;
            ans[i]=v[i];
            if(k==v[i]){
                k++;
            }
        }
        else{
            while(vis[k]){
                k++;
            }
            vis[k]=true;
            ans[i]=k;
            k++;

        }
    }
    for(auto &i:ans){
        cout<<i<<" ";
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

