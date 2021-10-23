/* Given an array arr of N integers. Find the contiguous 
sub-array with maximum sum. */

#include<bits/stdc++.h>
using namespace std;

void kadane(int ar[],int n)
{
    int cur_sum=0, sum=0;
    for(int i=0;i<n;i++)
    {
        cur_sum+=ar[i];
        if(cur_sum < 0 )
          cur_sum=0;
        if(cur_sum > sum)
         sum=cur_sum;
    }
    cout<<sum;
}

int main()
{
    int n;
    cin>>n;
    int ar[n];
    for(int i=0;i<n;i++)
    {
        cin>>ar[i];
    }
    kadane(ar,n);
}