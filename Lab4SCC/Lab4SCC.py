# Lab 4 Strongly Connected Components
# Alex Thayn 

from collections import defaultdict

#Take an adjacency list representation of a graph and returns a reversed graph
def reverseGraphAdjacencyList(adjacencyList):
    reversedList = defaultdict(list)
    for node1, values in adjacencyList.items():
        for value in values:
            reversedList[value].append(node1)
    return reversedList

#Take an adjacency list representation of a graph and performs a depth-first search (in linear time)

#Test reversed graph function
def test_reverseGraphAdjacencyList_directedGraph():
    adjList = [(1,2),(2,3),(4,5),(5,6),(6,4),(4,1)]
    originalGraph = defaultdict(list)
    for node1, node2 in adjList:
        originalGraph[node1].append(node2)
    
    reversedList = [(1,4),(2,1),(3,2),(4,6),(5,4),(6,5)]
    reversedGraph = defaultdict(list)
    for node1, node2 in reversedList:
        reversedGraph[node1].append(node2)

    assert reverseGraphAdjacencyList(originalGraph) == reversedGraph

def test_reverseGraphAdjacencyList_undirectedGraph():
    adjList = [(0,1),(0,4),(1,0),(1,4),(1,2),(1,3),(2,1),(2,3),(3,1),(3,4),(3,2),(4,3),(4,0),(4,1)]
    originalGraph = defaultdict(list)
    for node1, node2 in adjList:
        originalGraph[node1].append(node2)

    #ensure the reverse function returns the same list for an undirected graph
    #sorted the dictionaries so they would be comparable
    assert sorted(reverseGraphAdjacencyList(originalGraph)) == sorted(originalGraph)

#Test depth-first search function

if __name__ == "__main__":
    adjList = [(1,2),(2,3),(4,5),(5,6),(6,4),(4,1)]
    originalGraph = defaultdict(list)
    for node1, node2 in adjList:
        originalGraph[node1].append(node2)
    
    print("Original graph: ")
    print(originalGraph.items())

    reversedGraph = reverseGraphAdjacencyList(originalGraph)
    print("Reversed graph: ")
    print(reversedGraph.items())