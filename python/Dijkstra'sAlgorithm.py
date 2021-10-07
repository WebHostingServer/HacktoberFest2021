
import sys

class Graph :

    def __init__(self, vertices) :
        self.vertices = vertices
        self.adjMatrix = [[False for i in range(vertices)] for j in range(vertices)]

    def addEdge(self, v1, v2, dst) :
        self.adjMatrix[v1][v2] = self.adjMatrix[v2][v1] = dst

    def _getMinDistance(self, visited, distance) :

        min_distance = None
        for i in range(self.vertices) :
            if not visited[i] : 
                if min_distance is None : min_distance = i
                elif distance[min_distance] > distance[i] : min_distance = i

        return min_distance

    def _printPath(self, distance) :
        for i in range(self.vertices) : print(i, distance[i])

    def findPath(self) :

        distance, visited = [sys.maxsize for _ in range(self.vertices)], [False for _ in range(self.vertices)]

        distance[0] = 0        
        for i in range(self.vertices-1) :
            min_distance = self._getMinDistance(visited, distance)
            visited[min_distance] = True

            for j in range(self.vertices) :
                if not visited[j] and self.adjMatrix[min_distance][j] :
                    if self.adjMatrix[min_distance][j] + distance[min_distance] < distance[j] :
                        distance[j] = self.adjMatrix[min_distance][j] + distance[min_distance]

        self._printPath(distance)


v, e = map(int, input().split())

graph = Graph(v)
for _ in range(e) : 
    v1, v2, dst = map(int, input().split())
    graph.addEdge(v1, v2, dst)
graph.findPath()
