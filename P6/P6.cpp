#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fi first
#define se second

const int MOD = 998244353;
const int MAXN = 200005;	

// n^2(n+1)^2/4 - n(n+1)(2n+1)/6
// n(n+1)(n-1)(3n+2)/12

void solve(){
    int n; cin>>n;
    int temp = (((((n-1)*n/2)*(n+1))/3)*(3*n+2))/2;
    cout<<temp;
}

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int tc = 1;
    // cin >> tc;

    while(tc--){
        solve();
        cout << endl;
    }

    return 0;
}