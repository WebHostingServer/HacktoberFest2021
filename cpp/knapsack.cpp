#include<iostream>
using namespace std;


int knapsack(int * weights, int * profits, int n, int maxWeight) {
  
  int ** dp = new int * [n + 1];

  
  for (int i = 0; i < n + 1; i++) {

   
    dp[i] = new int[maxWeight + 1];
  }

  
  
  for (int i = 0; i < n + 1; i++) {
    
    for (int j = 0; j < maxWeight + 1; j++) {
      
      if (i == 0 || j == 0)
     
        dp[i][j] = 0;

      
      else if (weights[i - 1] > j) {
       
        dp[i][j] = dp[i - 1][j];
      } 
       else {

     
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + profits[i - 1]);

      }

    }

  
  }
  return dp[n][maxWeight];

}


int main() {

  
  int n;
  cout<<"enter number ";
  cin >> n;
  
  int * weights = new int[n];
  
  int * profits = new int[n];

  cout<<"enter weights: ";
  for (int i = 0; i < n; i++) {
    
    cin >> weights[i];
  }

  cout<<"enter profit: ";
  for (int i = 0; i < n; i++) {
    
    cin >> profits[i];
  }

  
  int maxWeight;
  cout<<"enter maximum weight : ";
  cin >> maxWeight;

  
  cout << knapsack(weights, profits, n, maxWeight);


}
