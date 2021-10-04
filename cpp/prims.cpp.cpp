// Implementation of Prim's algorithm for MST 
#include<bits/stdc++.h>
using namespace std;
# define INF 0x3f3f3f3f 

int main()
{
	int n = 6;
	vector<pair<int, int >> graph[n];// undirected graph
	graph[0].push_back({1,3});
	graph[1].push_back({0,3});
	graph[0].push_back({2,1});
	graph[2].push_back({0,1});
	graph[1].push_back({2,3});
	graph[2].push_back({1,3});
	graph[1].push_back({3,1});
	graph[3].push_back({1,1});
	graph[2].push_back({3,1});
	graph[3].push_back({2,1});
	graph[2].push_back({4,6});
	graph[4].push_back({2,6});
	graph[3].push_back({4,5});
	graph[4].push_back({3,5});
	graph[3].push_back({5,4});
	graph[5].push_back({3,4});
	graph[4].push_back({5,2});
	graph[5].push_back({4,2});
	
	priority_queue<pair<int , int>, vector<pair<int, int>> , greater<pair<int, int>> > pq; // syntax for minheap using priority queue, min key and source
	int src = 0;// source taken as vertex 0
	
	vector<int > key(n, INF);
	vector<int > parent(n, -1);
	vector<bool > inmst(n, false);

	pq.push({0, src});
	key[src] = 0;
	while(!pq.empty())
	{
		// extracting top vertes from priority queue
		int u = pq.top().second;// extract the top vertec which has the minimum key
		pq.pop();
	
		// include that vertex in mst
		inmst[u] = true;
		// explore children of that vertex
		for(int i=0;i<graph[u].size();i++)
		{
			int v = graph[u][i].first;
			int wt = graph[u][i].second;
			
			if(!inmst[v] && key[v]>wt)
			{
				key[v] = wt;
				parent[v] = u;
				pq.push({key[v],v});
			}
		}
	}
	for(int i=1;i<n;i++)
	{
		cout<<parent[i]<<" "<<i<<endl;
	}
	
	return 0;
}
