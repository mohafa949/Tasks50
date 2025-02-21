#include <iostream>
using namespace std;

int gcd(int a,int b)
{
    if (b==0 )
        return a;
    if (b>a)
        return gcd(b,a);
    return gcd(b,a-b);
}

int main(){
    int a,b;
    cout << "Enter an integer a : ";
    cin >> a;
    cout << "Enter an integer b : ";
    cin >> b;
    cout << "gcd(a,b) = "<<gcd(a,b);
    return 0;
}
