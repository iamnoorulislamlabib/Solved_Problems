// https://codeforces.com/problemset/problem/2061/B

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
    LL n;cin>>n;
    vector<LL>v(n);
    for(auto &i:v)cin>>i;
    LL x=-1,y=-1;
    sort(v.rbegin(),v.rend());
    for(LL i=0;i<(n-1);i++){
        if(v[i]==v[i+1]){
            x=v[i];
            y=v[i+1];
            v[i]=-1;
            v[i+1]=-1;
            break;
        }
    }
    // for(auto &i : v){
    //     cout<<i<<" ";
    // }
    //cout<<"\n";
    sort(v.rbegin(),v.rend());
    
    if(x==-1){
        cout<<-1<<"\n";
        return;
    }
    LL p=-1,q=-1;
    LL dif = LLONG_MAX;
    for(LL i=0;i<(n-1);i++){
        if(v[i]==-1 || v[i+1]==-1)continue;
        LL d = abs(v[i]-v[i+1]);
        if(d<dif){
            dif = d;
            p=v[i];
            q=v[i+1];
        }
    }
    //cout<<dif<<"\n";
    if(2*x <= dif){
        cout<<-1<<"\n";
        return;
    }

    cout<<x<<" "<<y<<" "<<p<<" "<<q<<"\n";

    
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

