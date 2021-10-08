#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int graph[100][100];

void dfs(int node, bool visited[], int n){

	if(visited[node])
		return ;

	visited[node] = true;
	printf("%c ",node+'A');

	//DFS traversal for each unvisited nodes
	for(int i = 0; i<n; i++){
		if(!visited[i] && graph[node][i]==1){
			dfs(i,visited,n);
		}
	}

}



int main()
{
    int nodes,edges;
    char start;
	printf("Enter number of nodes : ");
	scanf("%d",&nodes);

	//graph Input
	for(int i = 0; i<nodes; i++){
		for(int j = 0; j<nodes; j++){
			graph[i][j] = 0;
		}
	}

	printf("Enter the number of Edges : ");
	scanf("%d",&edges);

	//edges Input
	char a,b;
	for(int i = 0; i<edges; i++){
		scanf(" %c %c",&a,&b);
		//printf("%c %c",a,b);
		graph[a-'A'][b-'A'] = 1;
		//graph[b-'a'][a-'a'] = 1;
	}

	printf("Enter Start node : ");
	scanf(" %c",&start);

	//visited array
	bool visited[nodes];
	for(int i = 0; i<nodes; i++){
		visited[i] = false;
	}

	dfs(start-'A',visited,nodes);

	return 0;

}
