#include<iostream>
using namespace std;
int main()
{
    int n;
    int total = -1;
    cin >> n;
    for (int i = 0;i < n / 3 + 1;i++)
    {
        if ((n - 3 * i) % 5 == 0)
        {
            total += i + 1 + (n - 3 * i) / 5;
            break;
        }
    }
    cout << total << endl;
}