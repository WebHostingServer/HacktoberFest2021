/*Problem Statement - Given an array, print the Next Greater Element (NGE) for every element. 
The Next greater Element for an element x is the first greater element on the right side of x in the array. 
Elements for which no greater element exist, consider the next greater element as -1. */

//Problem Link - https://www.geeksforgeeks.org/next-greater-element/

#include<bits/stdc++.h>
using namespace std;
vector<int> nextLargerElement(vector<int> arr, int n)
{
        
        vector<int> ans(n);
        stack<int> st;
        st.push(n-1);
        ans[n-1]=-1;
        
        for(int i=n-2; i>=0; i--)
        {
            if(st.empty())
            {
                ans[i] = -1;
                st.push(i);
            }
            else
            {
                while(!st.empty() && arr[st.top()]<arr[i])
                {
                    st.pop();
                }
                if(st.empty())
                {
                    ans[i]=-1;
                }
                else
                {
                    ans[i] = arr[st.top()];
                }
                st.push(i);
            }
        }
        return ans;
}
int main()
{
    int n;
    cin>>n;

    vector<int> arr(n);
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }

    vector<int> ans = nextLargerElement(arr, n);
    for(int i=0; i<n; i++)
    {
        cout<<ans[i]<<" ";
    }
    cout<<endl;
}
