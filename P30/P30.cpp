#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fi first
#define se second

const int MOD = 998244353;
const int MAXN = 200005;
// const int pow = 4LL;

bool chk(int x){
	int temp = x;
	int sm = 0;
	while(temp){
		int y = temp%10;
		y = y*y*y*y*y;
		sm+=y;
		temp/=10;
	}

	return (sm==x);
}

// need to check only till 6*9^5, 
// we can reduce that bound more to 295277 and further
void solve(){
    int n; cin>>n;
    int ans = 0;
    for(int i=10; i<=n; i++){
    	if(chk(i)){
    		ans += i;
    	}
    }

    cout<<ans;
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