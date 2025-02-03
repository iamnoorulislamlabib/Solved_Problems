// https://codeforces.com/contest/2063/problem/B

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
    LL n,l,r;cin>>n>>l>>r;
    l--,r--;
    vector<LL>v(n);
    for(auto &i:v)cin>>i;
    vector<LL>v1,v2;
    for(LL i=0;i<l;i++){
        v1.push_back(v[i]);
    }
    for(LL i=r+1;i<n;i++){
        v2.push_back(v[i]);
    }
    if(v1.size()!=0)sort(v1.begin(),v1.end());
    if(v2.size()!=0)sort(v2.begin(),v2.end());
    
    vector<LL>ans1,ans2;
    LL dif = r-l+1;
    LL size1 = v1.size();
    LL size2 = v2.size();
    size1 = min(size1,dif);
    size2 = min(size2,dif);
    for(LL i=0;i<size1;i++){
        ans1.push_back(v1[i]);
    }
    for(LL i=l;i<=r;i++){
        ans1.push_back(v[i]);
        ans2.push_back(v[i]);
    }
    for(LL i=0;i<size2;i++){
        ans2.push_back(v2[i]);
    }

    sort(ans1.begin(),ans1.end());
    sort(ans2.begin(),ans2.end());
    LL res1 = 0;
    LL res2 = 0;
    for(LL i=0;i<dif;i++){
        res1+=ans1[i];
    }
    for(LL i=0;i<dif;i++){
        res2+=ans2[i];
    }
    LL res = min(res1,res2);
    cout<<res<<"\n";
    
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

