#include<bits/stdc++.h>
using namespace std;

#define pii pair<int,int>
int main()
{
	int n, m;
	cin >> n >> m;

	vector<vector<pii>> adj(n);

	for (int i = 0; i < m; i++)
	{
		int a, b, wt;
		cin >> a >> b >> wt;
		adj[a].push_back({b, wt});
	}
	vector<int> distance(n, INT_MAX);
	distance[0] = 0;

	set<pii> s;

	s.insert({0, 0});//dest,node

	while (!s.empty())
	{	auto node  = *s.begin();
		int v = node.second;
		int wt = node.first;
		s.erase(s.begin());
		for (auto x : adj[v])
		{
			if (wt + x.second < distance[x.first])
			{
				auto itr = s.find({distance[x.first], x.first});
				if (itr != s.end())
					s.erase(itr);
				distance[x.first] = wt + x.second;
				s.insert({distance[x.first], x.first});
			}

		}
	}
	int i = 0;
	for (auto x : distance)
		cout << "vertex(0)-->" << i++ << " " << x << endl;
	return 0;
}
