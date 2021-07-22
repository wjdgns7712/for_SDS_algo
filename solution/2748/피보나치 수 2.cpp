#include <bits/stdc++.h>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
#endif
    int n;
    scanf("%d", &n);
    long long int a=0, b=1, c=1;
    for(int i=0; i<n-1; i++){
        c=a+b;
        a=b;
        b=c;
    }
    printf("%lld", c);
    return 0;
}