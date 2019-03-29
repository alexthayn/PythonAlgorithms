from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable


def vars(s, low=None, high=None):
    """example creates three variables bounded from 0 to 10:
    a, b, c = vars('a,b,c', 0, 10)
    """
    return tuple(LpVariable(v.strip(), low, high) for v in s.split(','))


def lp(mode, objective, constraints):
    """see lp1 below for an example"""
    if mode.lower() == 'max':
        mode = LpMaximize
    elif mode.lower() == 'min':
        mode = LpMinimize
    prob = LpProblem("", mode)
    prob += objective
    for c in constraints:
        prob += c
    prob.solve()
    return prob, prob.objective.value(), dict((v.name, v.value()) for v in prob.variables())


def lp1():
    x_1, x_2 = vars('x_1, x_2')
    return lp('max', x_1 + 6*x_2, [
            x_1 >= 0,
            x_2 >= 0,
            x_1 <= 200,
            x_2 <= 300,
            x_1 + x_2 <= 400])

# Node class storing a node label and the neighboring input/output nodes
class Node:
    def __init__(self, label):
        self.label = label
        self.input = []
        self.output = []

# Class for storing our flow graph with nodes connected by weighted and directed edges
class LP_Graph:
    def __init__(self, source, target, nodes):
        self.source = source
        self.target = target
        self.input_vars = {}
        self.output_vars = {}
        self.edge_vars = {}
        self.nodes = nodes

    # Adds a weighted directed edge to the graph from node1 --> node2
    def addWeightedDirectedEdge(self, node1, node2, weight):
        self.edge_vars[(node1.label, node2.label)] = LpVariable(('e_' + node1.label + node2.label), 0, weight)
        # update input/output neighbors for each node
        node2.input.append(node2)
        node1.output.append(node1)

    # Generate a list of constraints for the max flow problem
    def getConstraints(self):
        constraintList = []
        # 1. output of the source node = input of target node
        constraintList.append(self.source.label)
    
def MaxFlow(graph):
    pass

if __name__ == "__main__":
    S = Node('S')
    T = Node('T')
    A = Node('A')
    B = Node('B')

    # Create a simple graph
    graph = LP_Graph(S,T,[S,T,A,B])
    graph.addWeightedDirectedEdge(S,B,1)
    graph.addWeightedDirectedEdge(A,B,4)
    graph.addWeightedDirectedEdge(S,B,2)
    graph.addWeightedDirectedEdge(A,T,2)
    graph.addWeightedDirectedEdge(B,T,3)

    for edge in graph.edge_vars.items():
        print(edge)

def testMaxFlow():
    S = Node('S')
    T = Node('T')
    A = Node('A')
    B = Node('B')

    # Create a simple graph
    graph = LP_Graph(S,T,[S,T,A,B])
    graph.addWeightedDirectedEdge(S,B,1)
    graph.addWeightedDirectedEdge(A,B,4)
    graph.addWeightedDirectedEdge(S,B,2)
    graph.addWeightedDirectedEdge(A,T,2)
    graph.addWeightedDirectedEdge(B,T,3)

    assert MaxFlow(graph) == 4