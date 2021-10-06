/** Bubble sort : compares two consecutive numbers,Bubble sort consists of n rounds. On each round, the algorithm iterates
through the elements of the array. Whenever two consecutive elements are found
that are not in correct order, the algorithm swaps them.
time complexity=> O(n)^2
Space complexity:**/

#include<bits\stdc++.h>
using namespace std;
int main()
{
	int t,n;
	cin>>t;
	while(t--)
	{
		cin>>n;
		int a[n];
		for(int i=0;i<n;i++)
		{
			cin>>a[i];
		}
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<n-1;k++)
			{
				if(a[k]>a[k+1])
				{
					swap(a[k],a[k+1]);
				}
			}
		}
		for(int l=0;l<n;l++)
		{
			cout<<a[l];
		}
	}
	return 0;
}
/*
Input: 
*/
