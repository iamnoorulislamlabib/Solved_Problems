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
    vector<vector<LL>>v(n,vector<LL>(m+1,-1));
    for(LL i=0;i<n;i++){
        v[i][0]=i;
        for(LL j=1;j<=m;j++){
            cin>>v[i][j];
        }
        sort(v[i].begin()+1,v[i].end());
    }

    sort(v.begin(),v.end(),cmp);

    // for(LL i=0;i<n;i++){
    //     for(LL j=0;j<=m;j++){
    //         cout<<v[i][j]<<" ";
    //     }
    //     cout<<"\n";
    // }

    LL mn = -1;
    for(LL j=1;j<=m;j++){
        if(j!=1){
            mn = v[n-1][j-1];
        }
        for(LL i=0;i<n-1;i++){
            if(i==0 and v[i][j]<mn){
                cout<<-1<<"\n";
                return;
            }
            if(v[i][j]>v[i+1][j]){
                cout<<-1<<"\n";
                return;
            }
            
        }
    }

    for(LL i=0;i<n;i++){
        cout<<(v[i][0]+1)<<" ";
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
