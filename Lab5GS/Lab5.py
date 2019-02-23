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

    def DFS1(self, source, target):
        stack = [(source, [source])]
        visited = set()

        while stack:
            (node, path) = stack.pop()
            if node not in visited:
                if node == target:
                    return path
                visited.add(node)
                for neighbor in self.graph[node]:
                    stack.append((neighbor, path + [neighbor]))

    # Breadth first search with a priority queue
    def BFS(self, source, target):
        queue = []
        queue.append([source])
        
        while len(queue) > 0:
            path = queue.pop(0)
            node = path[-1]
            if node == target:
                return path

            for neighbor in self.graph[node]:
                newPath = list(path)
                newPath.append(neighbor)
                queue.append(newPath)

    # Dijkstra's algorithm
    def Dijkstra(self, source, target):
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

    path = graph.DFS1(3, 6)
        
    while(len(path)>0):
        print(path.pop())

    path = graph.BFS(3,6)
    while(len(path)>0):
        print(path.pop())