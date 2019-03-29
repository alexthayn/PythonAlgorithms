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

        for e in nodes:
            self.input_vars[e.label] = LpVariable('i_' + e.label,0)
            self.output_vars[e.label] = LpVariable('o_' + e.label,0)

    # Adds a weighted directed edge to the graph from node1 --> node2
    def addWeightedDirectedEdge(self, node1, node2, weight):
        self.edge_vars[(node1.label, node2.label)] = ['e_' + node1.label + node2.label, weight]
        # update input/output neighbors for each node
        node2.input.append(node1)
        node1.output.append(node2)

    # Generate a list of constraints for the max flow problem
    def getConstraints(self):
        # constraintList = []
        # constraintList.append(f'o_{self.source.label} - i_{self.target.label} = 0')

        # 
        # for n in self.nodes:
        #     constraintList.append(f'i_{n.label} - o_{n.label} = 0')

        #
        # for n in self.nodes:
        #     singleConstraint = ''
        #     for inputNode in n.input:
        #         singleConstraint += f' + {self.edge_vars[inputNode.label,n.label][0]}'
        #     if(singleConstraint != ''):
        #         singleConstraint += f' = o_{n.label}'
        #         constraintList.append(singleConstraint)

        # # 4. node input = sum output edges of that node
        # for n in self.nodes:
        #     singleConstraint = ''
        #     for outputNode in n.output:
        #         singleConstraint += f' + {self.edge_vars[n.label,outputNode.label][0]}'
        #     if(singleConstraint != ''):
        #         singleConstraint += f' = i_{n.label}'
        #         constraintList.append(singleConstraint)

        # # 5. flow through edge <= max edge value
        # for edge in self.edge_vars.values():
        #     constraintList.append(f'{edge[0]} <= {edge[1]}')
        
        # print(constraintList)
        # return constraintList

        constraints = []

        # 1. output of the source node = input of target node
        constraints.append(self.input_vars[self.source.label] == self.output_vars[self.target.label])

        # 2. each nodes input = each nodes output
        constraints.extend(self.input_vars[v.label] == self.output_vars[v.label] for v in self.nodes)

        # 3. sum input edges to node = node output
        constraints.extend(self.input_vars[v.label] == sum(self.edge_vars[(neighbor.label,v.label)][1] for neighbor in v.input) for v in self.nodes)

        # 4. node input = sum output edges of that node
        constraints.extend(self.output_vars[v.label] == sum(self.edge_vars[(v.label, neighbor.label)][1] for neighbor in v.output) for v in self.nodes)

        print(constraints)
        return constraints

def MaxFlow(graph):
    return lp('max', graph.input_vars[graph.target.label],graph.getConstraints())

if __name__ == "__main__":
    S = Node('S')
    T = Node('T')
    A = Node('A')
    B = Node('B')

    # Create a simple graph
    graph = LP_Graph(S,T,[S,T,A,B])
    graph.addWeightedDirectedEdge(S,A,2)
    graph.addWeightedDirectedEdge(A,B,4)
    graph.addWeightedDirectedEdge(S,B,2)
    graph.addWeightedDirectedEdge(A,T,2)
    graph.addWeightedDirectedEdge(B,T,3)

    for edge in graph.edge_vars.items():
        print(edge)

    graph.getConstraints()

    print(MaxFlow(graph))

def testMaxFlow():
    S = Node('S')
    T = Node('T')
    A = Node('A')
    B = Node('B')

    # Create a simple graph
    graph = LP_Graph(S,T,[S,T,A,B])
    graph.addWeightedDirectedEdge(S,A,2)
    graph.addWeightedDirectedEdge(A,B,4)
    graph.addWeightedDirectedEdge(S,B,2)
    graph.addWeightedDirectedEdge(A,T,2)
    graph.addWeightedDirectedEdge(B,T,3)

    assert MaxFlow(graph) == 4