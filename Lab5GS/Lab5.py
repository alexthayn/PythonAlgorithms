# Alex Thayn
# Lab 5: Graph Search

from boltons.queueutils import PriorityQueue
from collections import defaultdict

#Graph class that contains graph search functions taht operate on it
class Graph:
    def __init__(self):
        #using defaultdict to store an adjacency list
        self.graph = defaultdict(list)

    def addEdge(self, node1, node2):
        self.graph[node1].append(node2)

    # Depth first search with a priority queue
    def DFS(self, source, target):
        visited = []
        pq = PriorityQueue()
        pq.add(source)
        while len(pq) > 0:
            node = pq.pop()
            if node not in visited:
                if node == target:
                    return pq
                visited.append(node)
                for neighbor in self.graph[node]:
                    pq.add(neighbor)
        #self.DFS_Recursive(firstNode, visited)


    def DFS_Recursive(self, node, visited):
        visited[node] = True
        print(node)

        for neighbor in self.graph[node]:
            print("neighbor:" ,neighbor)
            if visited[neighbor] == False:
                self.DFS_Recursive(neighbor, visited)

    # Breadth first search with a priority queue
    def BFS(self):
        pass

    # Dijkstra's algorithm
    def Dijkstra(self):
        pass

    # A* algorithm
    def AStar(self):
        pass    

if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(1,2)
    graph.addEdge(1,3)
    graph.addEdge(2,1)
    graph.addEdge(2,5)
    graph.addEdge(2,4)
    graph.addEdge(3,1)
    graph.addEdge(3,5)
    graph.addEdge(4,2)
    graph.addEdge(4,6)
    graph.addEdge(4,5)
    graph.addEdge(5,2)
    graph.addEdge(5,3)
    graph.addEdge(5,4)
    graph.addEdge(5,6)
    graph.addEdge(6,4)

    path = graph.DFS(2, 6)
        
    while(len(path)>0):
        print(path.pop())